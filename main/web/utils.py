from sqlalchemy.orm import joinedload
from main.models import Page

def get_all_data():
	data = {}
	pages = Page.query.options(
		joinedload(Page.Category),
		joinedload(Page.Collection)
	)\
		.filter(Page.deleted != 1)\
		.all()
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
				collection_data["category_name"] = collection.category.category_name if collection.category else ''
				collection_data["category_id"] = collection.category.id if collection.category else ''
				collection_data["images"] = [image.to_json_api() for image in collection.Image]
				collections_list.append(collection_data)

			category_data["collections"] = collections_list
			categories_list.append(category_data)
		page_data["categories"] = categories_list

		images_list = []
		for image in page.Image:
			image_data = image.to_json_api()
			image_data["category_name"] = image.category.category_name if image.category else ''
			#image_data["images"] = [image.to_json_api() for image in image.Image]
			images_list.append(image_data)
		page_data["images"] = images_list

		collections_list = []
		for collection in page.Collection:
			collection_data = collection.to_json_api()
			collection_data["category_name"] = collection.category.category_name if collection.category else ''
			collection_data["images"] = [image.to_json_api() for image in collection.Image]
			collections_list.append(collection_data)
		page_data["collections"] = collections_list
			
		data[page.page_name] = page_data



		#collections_list = []
		#for collection in page.Collection:
		#	collection_data = collection.to_json_api()
		#	collection_data["category_name"] = collection.category.name_tk if collection.category else ''
		#	collection_data["category_id"] = collection.category.id if collection.category else ''
		#	collection_data["images"] = [image.to_json_api() for image in collection.Image]
		#	collections_list.append(collection_data)
		
		#page_data["collections"] = collections_list

		#data[page.name_tk] = page_data


	return data
		