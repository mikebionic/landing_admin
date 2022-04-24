
from main.models import Page

def get_all_data():
	data = {}
	pages = Page.query.all()
	for page in pages:
		page_data = page.to_json_api()
		page_data["images"] = [image.to_json_api() for image in page.Image]
		page_data["categories"] = [category.to_json_api() for category in page.Category]
		# page_data["collections"] = [collection.to_json_api() for collection in page.Collection]

		collections_list = []
		for collection in page.Collection:
			collection_data = collection.to_json_api()
			collection_data["category_name"] = collection.category.name if collection.category else ''
			collection_data["images"] = [image.to_json_api() for image in collection.Image]
			collections_list.append(collection_data)
		
		page_data["collections"] = collections_list

		data[page.name] = page_data

	return data
		