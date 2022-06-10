
from main import db
from main.config import Config
from main.models import BaseModel


class Page(BaseModel, db.Model):
	__tablename__ = "tbl_page"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	page_name = db.Column("page_name",db.String,nullable=False)
	Collection = db.relationship("Collection",backref='page',lazy=True)
	Category = db.relationship("Category",backref='page',lazy=True)
	Contact = db.relationship("Contact",backref='page',lazy=True)
	Image = db.relationship("Image",backref='page',lazy='joined')

	def to_json_api(self):
		data = {
			"id": self.id,
			"page_name": self.page_name,
		}
		for key, value in BaseModel.to_json(self).items():
			data[key] = value
		return data
		
	def collect_page_data(db_model):
		page_data = db_model.to_json_api()
		page_data["categories"] = [category.to_json_api() for category in db_model.Category]

		images_list = []
		for image in db_model.Image:
			image_data = image.to_json_api()
			image_data["category_name"] = image.category.category_name if image.category else ''
			#image_data["images"] = [image.to_json_api() for image in image.Image]
			images_list.append(image_data)
		page_data["images"] = images_list

		collections_list = []
		for collection in db_model.Collection:
			collection_data = collection.to_json_api()
			collection_data["category_name"] = collection.category.category_name if collection.category else ''
			collection_data["images"] = [image.to_json_api() for image in collection.Image]
			collections_list.append(collection_data)

		page_data["collections"] = collections_list
		return page_data

	def get_related_data(id = None, data_type="list"):
		if id:
			page = Page.query.get(id)
			return Page.collect_page_data(page)
		
		else:
			pages = Page.query.filter(Page.deleted != 1).all()
			if data_type == "list":
				data = []
				for page in pages:
					data.append(Page.collect_page_data(page))

			if data_type == "object":
				data = {}
				for page in pages:
					page_data = Page.collect_page_data(page)
					data[page_data["page_name"]] = page_data
			return data
