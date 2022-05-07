
from main.models import Page

def get_all_data():
	data = {}
	pages = Page.query.all()
	for page in pages:
		page_data = page.to_json_api()
		page_data["images"] = [image.to_json_api() for image in page.Image]
		page_data["contacts"] = [contact.to_json_api() for contact in page.Contact]

		categories_list = []
		for category in page.Category:
			category_data = category.to_json_api()
			collections_list = []
			for collection in category.Collection:
				collection_data = collection.to_json_api()
				collection_data["category_name"] = collection.category.name_tk if collection.category else ''
				collection_data["images"] = [image.to_json_api() for image in collection.Image]
				collections_list.append(collection_data)
				category_data["collections"] = collections_list

			categories_list.append(category_data)
		
		page_data["categories"] = categories_list

		collections_list = []
		for collection in page.Collection:
			collection_data = collection.to_json_api()
			collection_data["category_name"] = collection.category.name_tk if collection.category else ''
			collection_data["images"] = [image.to_json_api() for image in collection.Image]
			collections_list.append(collection_data)
		
		page_data["collections"] = collections_list


		data[page.name_tk] = page_data

	return data
		