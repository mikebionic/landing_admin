from flask import make_response, request

from . import api
from .controllers import get_pages, get_images

@api.route("/get-pages/")
def pages():
	id = request.args.get("id",0,type=int)
	page_name = request.args.get("page_name","",type=str)
	single_object = request.args.get("single_object",0,type=int)
	data, message = get_pages(id, page_name, single_object)
	return {
		"data": data,
		"message": message,
	}



@api.route("/get-images/")
def images():
	id = request.args.get("id",0,type=int)
	page_id = request.args.get("page_id",0,type=int)
	category_id = request.args.get("category_id",0,type=int)
	category_name = request.args.get("category_name","",type=str)
	data, message = get_images(id, page_id, category_id, category_name)
	return {
		"data": data,
		"message": message,
	}

