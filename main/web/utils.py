
from main.models import Page

def get_all_data():
	data = {}
	pages = Page.query.all()
	for page in pages:
		page_data = page.to_json_api()
		page_data["images"] = [image.to_json_api() for image in page.Image]
		page_data["categories"] = [category.to_json_api() for category in page.Category]
		page_data["collections"] = [collection.to_json_api() for collection in page.Collection]
		data[page.name] = page_data
	
	return data
		