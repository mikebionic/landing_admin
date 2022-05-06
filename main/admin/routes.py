from flask import render_template, request, redirect, url_for
from flask_login import login_required

from . import bp

from main import db
from main.models import Page, Collection, Category, Contact, Image
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

	elif data_type == "images":
		data = Image.get_all(Image)
		return render_template('admin/images_list.html', data=data, data_type=data_type)

	else:
		return redirect(url_for('admin.dashboard'))

	return render_template('admin/dashboard.html', data=data, data_type=data_type)


@bp.route("/<data_type>/<id>/manage/")
@login_required
def manage_data(data_type, id):
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
		return render_template('admin/manage_image.html', data=data, data_type=data_type)

	return render_template('admin/manage_data.html', data=data, data_type=data_type)


@bp.route("/<data_type>/<id>/manage/", methods=["POST"])
@login_required
def manage_data_post(data_type, id):
	request_data = add_data_from_form(request, data_type)

	if data_type == 'pages':
		db_model = Page.query.get_or_404(id)

	if data_type == "collections":
		db_model = Collection.query.get_or_404(id)

	if data_type == "categories":
		db_model = Category.query.get_or_404(id)

	if data_type == "contacts":
		db_model = Contact.query.get_or_404(id)

	db_model.update(**request_data)
	db.session.commit()
	return redirect(url_for('admin.manage_data', data_type=data_type, id=id))


@bp.route("/<data_type>/add/")
@login_required
def add_data_get(data_type):
	if data_type == "images":
		return render_template('admin/add_image.html', data_type=data_type)
	return render_template('admin/add_data.html', data_type=data_type)

@bp.route("/<data_type>/add/", methods=["POST"])
@login_required
def add_data_post(data_type):
	request_data = {}
	if "name" in request.form:
		request_data["name"] = request.form["name"]
	if "title" in request.form:
		request_data["title"] = request.form["title"]
	if "label" in request.form:
		request_data["label"] = request.form["label"]
	if "desc" in request.form:
		request_data["desc"] = request.form["desc"]
	if "html" in request.form:
		request_data["html"] = request.form["html"]

	if data_type == 'pages':
		DbModel = Page
	if data_type == "collections":
		DbModel = Collection
	if data_type == "categories":
		DbModel = Category
	if data_type == "contacts":
		DbModel = Contact

	lastId_model = DbModel.query.with_entities(DbModel.id).order_by(DbModel.id.desc()).first()
	if lastId_model:
		request_data['id'] = lastId_model.id + 1
	db_model = DbModel(**request_data)

	db.session.add(db_model)
	db.session.commit()
	return redirect(url_for('admin.dashboard', data_type=data_type))

