from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from main import db
from main.config import Config


class Text_data(db.Model):
	__tablename__ = "tbl_text_data"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	name_en = db.Column("name_en",db.String)
	name_ru = db.Column("name_ru",db.String)
	name_tk = db.Column("name_tk",db.String)
	label_en = db.Column("label_en",db.String)
	label_ru = db.Column("label_ru",db.String)
	label_tk = db.Column("label_tk",db.String)
	title_en = db.Column("title_en",db.String)
	title_ru = db.Column("title_ru",db.String)
	title_tk = db.Column("title_tk",db.String)
	desc_en = db.Column("desc_en",db.String)
	desc_ru = db.Column("desc_ru",db.String)
	desc_tk = db.Column("desc_tk",db.String)
	html_en = db.Column("html_en",db.String)
	html_ru = db.Column("html_ru",db.String)
	html_tk = db.Column("html_tk",db.String)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())
	Category = db.relationship("Category",backref='text_data',lazy=True)
	Collection = db.relationship("Collection",backref='text_data',lazy=True)
	Contact = db.relationship("Contact",backref='text_data',lazy=True)
	Page = db.relationship("Page",backref='text_data',lazy=True)
	Image = db.relationship("Image",backref='text_data',lazy=True)

	def to_json_api(self):
		return {
			"id": self.id,
			"guid": self.guid,
			"name_en": self.name_en,
			"name_ru": self.name_ru,
			"name_tk": self.name_tk,
			"label_en": self.label_en,
			"label_ru": self.label_ru,
			"label_tk": self.label_tk,
			"title_en": self.title_en,
			"title_ru": self.title_ru,
			"title_tk": self.title_tk,
			"desc_en": self.desc_en,
			"desc_ru": self.desc_ru,
			"desc_tk": self.desc_tk,
			"html_en": self.html_en,
			"html_ru": self.html_ru,
			"html_tk": self.html_tk,
			"created_date": self.created_date,
		}