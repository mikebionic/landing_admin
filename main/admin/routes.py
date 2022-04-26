from flask import render_template, request, redirect, url_for
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
		
		page.update(**request_data)
	
	return redirect(url_for('admin.manage_data', data_type=data_type, id=id))