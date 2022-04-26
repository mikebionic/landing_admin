
from main import db
from main.config import Config
from main.models import BaseModel


class Collection(BaseModel, db.Model):
	__tablename__ = "tbl_collection"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	category_id = db.Column("category_id",db.Integer,db.ForeignKey("tbl_category.id"))
	text_data_id = db.Column("text_data_id",db.Integer,db.ForeignKey("tbl_text_data.id"))
	Image = db.relationship("Image",backref='collection',lazy='joined')

	def to_json_api(self):
		data = {
			"id": self.id,
			"page_id": self.page_id,
			"category_id": self.category_id,
		}
		for key, value in BaseModel.to_json(self).items():
			data[key] = value
		return data