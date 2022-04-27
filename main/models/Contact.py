
from main import db
from main.config import Config
from main.models import BaseModel


class Contact(BaseModel, db.Model):
	__tablename__ = "tbl_contact"
	id = db.Column("id",db.Integer,nullable=False,primary_key=True)
	page_id = db.Column("page_id",db.Integer,db.ForeignKey("tbl_page.id"))
	text_data_id = db.Column("text_data_id",db.Integer,db.ForeignKey("tbl_text_data.id"))

	phone_number = db.Column("phone_number",db.String)
	home_phone_number = db.Column("home_phone_number",db.String)
	work_phone_number = db.Column("work_phone_number",db.String)
	phone_number_1 = db.Column("phone_number_1",db.String)
	phone_number_2 = db.Column("phone_number_2",db.String)
	phone_number_3 = db.Column("phone_number_3",db.String)
	mail = db.Column("mail",db.String)
	mail_1 = db.Column("mail_1",db.String)
	mail_2 = db.Column("mail_2",db.String)
	mail_3 = db.Column("mail_3",db.String)
	address = db.Column("address",db.String)
	address_1 = db.Column("address_1",db.String)
	address_2 = db.Column("address_2",db.String)
	address_3 = db.Column("address_3",db.String)
	social_1_name = db.Column("social_1_name",db.String)
	social_1 = db.Column("social_1",db.String)
	social_2_name = db.Column("social_2_name",db.String)
	social_2 = db.Column("social_2",db.String)
	social_3_name = db.Column("social_3_name",db.String)
	social_3 = db.Column("social_3",db.String)

	def to_json_api(self):
		data = {
			"id": self.id,
			"page_id": self.page_id,
			"phone_number": self.phone_number,
			"home_phone_number": self.home_phone_number,
			"work_phone_number": self.work_phone_number,
			"phone_number_1": self.phone_number_1,
			"phone_number_2": self.phone_number_2,
			"phone_number_3": self.phone_number_3,
			"mail": self.mail,
			"mail_1": self.mail_1,
			"mail_2": self.mail_2,
			"mail_3": self.mail_3,
			"address": self.address,
			"address_1": self.address_1,
			"address_2": self.address_2,
			"address_3": self.address_3,
			"social_1_name": self.social_1_name,
			"social_1": self.social_1,
			"social_2_name": self.social_2_name,
			"social_2": self.social_2,
			"social_3_name": self.social_3_name,
			"social_3": self.social_3,
		}
		for key, value in BaseModel.to_json(self).items():
			data[key] = value
		return data
