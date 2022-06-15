from flask import render_template, request, redirect, url_for
from flask_login import login_required

from . import bp

from main import db
from main.models import Page, Collection, Category, Contact, Image, User
from main.admin.utils import add_data_from_form


@bp.route("/")
@bp.route("/dashboard/")
@bp.route("/<data_type>/")
@login_required
def dashboard(data_type="pages"):
	data = {}
	if data_type == "pages":
		data = Page.get_all(Page)

	elif data_type == "collections":
		data = Collection.get_all(Collection)

	elif data_type == "categories":
		data = Category.get_all(Category)

	elif data_type == "contacts":
		data = Contact.get_all(Contact)

	elif data_type == "users":
		data = [user.to_json_api() for user in User.query.all()]

	elif data_type == "images":
		data = Image.get_all(Image)
		return render_template('admin/images_list.html', data=data, data_type=data_type)

	else:
		return redirect(url_for('admin.dashboard'))

	return render_template('admin/dashboard.html', data=data, data_type=data_type)


@bp.route("/<data_type>/<id>/manage/")
@login_required
def manage_data(data_type, id):
	all_data = {
		"pages": Page.query.all(),
		"collections": Collection.query.all(),
		"categories": Category.query.all(),
		"contacts": Contact.query.all(),
	}
	if data_type == 'pages':
		data = Page.get_related_data(id)

	if data_type == "collections":
		data = Collection.query.get_or_404(id)
		data = data.to_json_api()

	if data_type == "categories":
		data = Category.query.get_or_404(id)
		data = data.to_json_api()

	if data_type == "contacts":
		data = Contact.query.get_or_404(id)
		data = data.to_json_api()

	if data_type == "images":
		data = Image.query.get_or_404(id)
		data = data.to_json_api()
		return render_template('admin/manage_image.html', data=data, data_type=data_type, **all_data)

	if data_type == "users":
		data = User.query.get_or_404(id)
		data = data.to_json_api()
		return render_template('admin/manage_user.html', data=data, data_type=data_type, **all_data)

	return render_template('admin/manage_data.html', data=data, data_type=data_type, **all_data)


@bp.route("/<data_type>/<id>/manage/", methods=["POST"])
@login_required
def manage_data_post(data_type, id):
	request_data = add_data_from_form(request, data_type)
	db_model = get_db_model_from_data_type_and_id(data_type, id)
	db_model.update(**request_data)
	db.session.commit()
	return redirect(url_for('admin.manage_data', data_type=data_type, id=id))


@bp.route("/<data_type>/add/")
@login_required
def add_data_get(data_type):
	if data_type == "images":
		return render_template('admin/add_image.html', data_type=data_type)
	if data_type == "users":
		return render_template('admin/add_user.html', data_type=data_type)
	return render_template('admin/add_data.html', data_type=data_type)


@bp.route("/<data_type>/<id>/delete/")
@login_required
def delete_data_get(data_type, id):
	db_model = get_db_model_from_data_type_and_id(data_type, id)
	db_model.deleted = 1
	db.session.commit()
	return redirect(url_for('admin.dashboard', data_type=data_type))


@bp.route("/<data_type>/<id>/restore/")
@login_required
def restore_data_get(data_type, id):
	db_model = get_db_model_from_data_type_and_id(data_type, id)
	db_model.deleted = 0
	db.session.commit()
	return redirect(url_for('admin.dashboard', data_type=data_type))


def get_db_model_from_data_type_and_id(data_type, id):
	db_model = None
	if data_type == 'pages':
		db_model = Page.query.get_or_404(id)

	if data_type == "collections":
		db_model = Collection.query.get_or_404(id)

	if data_type == "categories":
		db_model = Category.query.get_or_404(id)

	if data_type == "contacts":
		db_model = Contact.query.get_or_404(id)

	if data_type == "images":
		db_model = Image.query.get_or_404(id)

	if data_type == "users":
		db_model = User.query.get_or_404(id)
	return db_model

@bp.route("/<data_type>/add/", methods=["POST"])
@login_required
def add_data_post(data_type):
	request_data = add_data_from_form(request, data_type)

	if data_type == 'pages':
		DbModel = Page
	if data_type == "collections":
		DbModel = Collection
	if data_type == "categories":
		DbModel = Category
	if data_type == "contacts":
		DbModel = Contact
	if data_type == "images":
		db_model = Image
	if data_type == "users":
		db_model = User

	lastId_model = DbModel.query.with_entities(DbModel.id).order_by(DbModel.id.desc()).first()
	if lastId_model:
		request_data['id'] = lastId_model.id + 1
	db_model = DbModel(**request_data)
	db.session.add(db_model)
	db.session.commit()
	return redirect(url_for('admin.dashboard', data_type=data_type))

