from flask import render_template
from flask_login import login_required

from . import bp

from main.models import Page


@bp.route("/")
@bp.route("/dashboard/")
@login_required
def dashboard():
	pages = Page.get_all()
	return render_template('admin/dashboard.html', data=pages)


@bp.route("/<data_type>/<id>/manage/")
@login_required
def manage_data(data_type, id):
	if data_type == 'page':
		page = Page.get_related_data(id)

	return render_template('admin/manage_data.html', data=page)


@bp.route("/<data_type>/<id>/manage/", methods=["POST"])
@login_required
def manage_data_post(data_type, id):
	if data_type == 'page':
		page = Page.query.get(id)
	
	return render_template('admin/manage_data.html', data=page)