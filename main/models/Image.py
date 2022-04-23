from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from main import db
from main.config import Config


class Image(db.Model):
	__tablename__ = "tbl_image"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	category_id = db.Column("category_id",db.Integer,db.ForeignKey("tbl_category.id"))
	collection_id = db.Column("collection_id",db.Integer,db.ForeignKey("tbl_collection.id"))
	text_data_id = db.Column("text_data_id",db.Integer,db.ForeignKey("tbl_text_data.id"))
	contact_id = db.Column("contact_id",db.Integer,db.ForeignKey("tbl_contact.id"))
	file_path = db.Column("file_path",db.String)
	file_path_m = db.Column("file_path_m",db.String)
	file_path_s = db.Column("file_path_s",db.String)
	link = db.Column("link",db.String)
	name = db.Column("name",db.String)
	label = db.Column("label",db.String)
	title = db.Column("title",db.String)
	desc = db.Column("desc",db.String)
	html = db.Column("html",db.String)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())

	def to_json_api(self):
		return {
			"id": self.id,
			"guid": self.guid,
			"page_id": self.page_id,
			"category_id": self.category_id,
			"collection_id": self.collection_id,
			"text_data_id": self.text_data_id,
			"contact_id": self.contact_id,
			"file_path": self.file_path,
			"file_path_m": self.file_path_m,
			"file_path_s": self.file_path_s,
			"link": self.link,
			"name": self.name,
			"label": self.label,
			"title": self.title,
			"desc": self.desc,
			"html": self.html,
			"created_date": self.created_date,
		}