from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from main import login_manager
from main import db
from main.config import Config


@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model, UserMixin):
	__tablename__ = "tbl_user"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	guid = db.Column("guid",UUID(as_uuid=True),unique=True,default=uuid.uuid4())
	name = db.Column("name",db.String(100))
	username = db.Column("username",db.String(60),nullable=False)
	email = db.Column("email",db.String(100),unique=True)
	password = db.Column("password",db.String(60),nullable=False)
	type_id = db.Column("type_id",db.Integer)
	created_date = db.Column("created_date",db.DateTime,default=datetime.now())

	def is_admin(self):
		return self.type_id == 1

	def get_id(self):
		return (self.id)

	def to_json_api(self):
		return {
			"id": self.id,
			"guid": self.guid,
			"name": self.name,
			"username": self.username,
			"email": self.email,
			"password": self.password,
			"type_id": self.type_id,
			"created_date": self.created_date,
		}