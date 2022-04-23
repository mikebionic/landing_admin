from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from main import db
from main.config import Config


class Collection(db.Model):
	__tablename__ = "tbl_collection"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	category_id = db.Column("category_id",db.Integer,db.ForeignKey("tbl_category.id"))
	text_data_id = db.Column("text_data_id",db.Integer,db.ForeignKey("tbl_text_data.id"))
	name = db.Column("name",db.String)
	label = db.Column("label",db.String)
	title = db.Column("title",db.String)
	desc = db.Column("desc",db.String)
	html = db.Column("html",db.String)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())
	Image = db.relationship("Image",backref='collection',lazy='joined')

	def to_json_api(self):
		return {
			"id": self.id,
			"guid": self.guid,
			"page_id": self.page_id,
			"category_id": self.category_id,
			"name": self.name,
			"label": self.label,
			"title": self.title,
			"desc": self.desc,
			"html": self.html,
			"created_date": self.created_date,
		}