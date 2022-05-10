from main import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from main.languageMethods import dataLangSelector

class BaseModel(object):
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	name_tk = db.Column("name_tk",db.String)
	name_ru = db.Column("name_ru",db.String)
	name_en = db.Column("name_en",db.String)

	label_tk = db.Column("label_tk",db.String)
	label_ru = db.Column("label_ru",db.String)
	label_en = db.Column("label_en",db.String)

	title_tk = db.Column("title_tk",db.String)
	title_ru = db.Column("title_ru",db.String)
	title_en = db.Column("title_en",db.String)

	desc_tk = db.Column("desc_tk",db.String)
	desc_ru = db.Column("desc_ru",db.String)
	desc_en = db.Column("desc_en",db.String)

	html_tk = db.Column("html_tk",db.String)
	html_ru = db.Column("html_ru",db.String)
	html_en = db.Column("html_en",db.String)

	note_tk = db.Column("note_tk",db.String)
	note_ru = db.Column("note_ru",db.String)
	note_en = db.Column("note_en",db.String)

	link = db.Column("link",db.String)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())
	deleted = db.Column("deleted",db.Integer,default=0)

	def get_all(self):
		db_models = self.query.order_by(self.id.asc()).all()
		return [item.to_json_api() for item in db_models]

	@property
	def is_deleted(self):
		return 1 if self.deleted else 0

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

	def to_json(self):
		data = {
			"name_tk": self.name_tk,
			"name_ru": self.name_ru,
			"name_en": self.name_en,

			"label_tk": self.label_tk,
			"label_ru": self.label_ru,
			"label_en": self.label_en,

			"title_tk": self.title_tk,
			"title_ru": self.title_ru,
			"title_en": self.title_en,

			"desc_tk": self.desc_tk,
			"desc_ru": self.desc_ru,
			"desc_en": self.desc_en,

			"html_tk": self.html_tk,
			"html_ru": self.html_ru,
			"html_en": self.html_en,

			"note_tk": self.note_tk,
			"note_ru": self.note_ru,
			"note_en": self.note_en,

			"link": self.link,
			"created_date": self.created_date,
			"deleted": self.deleted,
		}
		translated = dataLangSelector(data)
		for k, v in translated.items():
			data[k] = v
		return data