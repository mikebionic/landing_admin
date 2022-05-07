from main import db
from main.config import Config
from main.models import BaseModel


class Category(BaseModel, db.Model):
	__tablename__ = "tbl_category"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	Collection = db.relationship("Collection",backref='category',lazy=True)
	Image = db.relationship("Image",backref='category',lazy="joined")

	def to_json_api(self):
		data = {
			"id": self.id,
			"page_id": self.page_id,
		}
		for key, value in BaseModel.to_json(self).items():
			data[key] = value
		return data