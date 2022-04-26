from main import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BaseModel(object):
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	name = db.Column("name",db.String)
	label = db.Column("label",db.String)
	title = db.Column("title",db.String)
	desc = db.Column("desc",db.String)
	html = db.Column("html",db.String)
	link = db.Column("link",db.String)
	note = db.Column("note",db.String)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())
	deleted = db.Column("deleted",db.Integer,default=None)

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
		return {
			"name": self.name,
			"label": self.label,
			"title": self.title,
			"desc": self.desc,
			"html": self.html,
			"link": self.link,
			"note": self.note,
			"created_date": self.created_date,
			"deleted": self.deleted,
		}
