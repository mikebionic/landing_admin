from main.models import (
	Image,
	Page,
	Collection,
	Category,
)

def get_pages(id=None, page_name="", single_object=0):
	data, message = [], "Pages"
	filtering = {
		"deleted": 0,
	}
	if id:
		filtering["id"] = id

	try:
		db_models = Page.query.filter_by(**filtering)\
			.filter(Page.page_name.ilike(f"%{page_name}%"))

		db_models = db_models.first() if single_object else db_models.all()

		if not db_models:
			message = "Not found"
			raise Exception(message)

		data = db_models.collect_page_data() if single_object else [db_model.collect_page_data() for db_model in db_models]
	
	except Exception as e:
		print(e)
	
	return data, message

def get_images(id=None, page_id = None, category_id = None, category_name=""):
	data, message = [], "Images"
	filtering = {
		"deleted": 0,
	}
	if id:
		filtering["id"] = id
	if page_id:
		filtering["page_id"] = page_id
	if category_id:
		filtering["category_id"] = category_id

	try:
		category_ids = []
		if category_name:
			category_models = Category.query.with_entities(Category.id, Category.category_name)\
				.filter(Category.category_name.ilike(f"%{category_name}%"))\
				.all()
			if not category_models:
				message = "Categories not found from your search"
				raise Exception(message)
			if category_models:
				category_ids = [category_model.id for category_model in category_models]

		db_models = Image.query.filter_by(**filtering)
		if category_ids:
			db_models = db_models.filter(Image.category_id.in_(category_ids))
		db_models = db_models.all()

		if not db_models:
			message = "Not found"
			raise Exception(message)

		data = [db_model.to_json_api() for db_model in db_models]
	
	except Exception as e:
		print(e)
	
	return data, message
