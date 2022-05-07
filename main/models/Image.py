
from main import db
from main.config import Config
from main.models import BaseModel

class Image(BaseModel, db.Model):
	__tablename__ = "tbl_image"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	category_id = db.Column("category_id",db.Integer,db.ForeignKey("tbl_category.id"))
	collection_id = db.Column("collection_id",db.Integer,db.ForeignKey("tbl_collection.id"))
	contact_id = db.Column("contact_id",db.Integer,db.ForeignKey("tbl_contact.id"))
	file_path = db.Column("file_path",db.String)
	file_path_m = db.Column("file_path_m",db.String)
	file_path_s = db.Column("file_path_s",db.String)

	def to_json_api(self):
		data = {
			"id": self.id,
			"page_id": self.page_id,
			"category_id": self.category_id,
			"collection_id": self.collection_id,
			"contact_id": self.contact_id,
			"file_path": self.file_path,
			"file_path_m": self.file_path_m,
			"file_path_s": self.file_path_s,
		}

		for key, value in BaseModel.to_json(self).items():
			data[key] = value
		return data