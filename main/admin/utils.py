import os
from main.config import Config

def add_data_from_form(request, data_type=None):
	request_data = {}
	if "name_tk" in request.form:
		request_data["name_tk"] = request.form["name_tk"]
	if "name_ru" in request.form:
		request_data["name_ru"] = request.form["name_ru"]
	if "name_en" in request.form:
		request_data["name_en"] = request.form["name_en"]

	if "title_tk" in request.form:
		request_data["title_tk"] = request.form["title_tk"]
	if "title_ru" in request.form:
		request_data["title_ru"] = request.form["title_ru"]
	if "title_en" in request.form:
		request_data["title_en"] = request.form["title_en"]

	if "label_tk" in request.form:
		request_data["label_tk"] = request.form["label_tk"]
	if "label_ru" in request.form:
		request_data["label_ru"] = request.form["label_ru"]
	if "label_en" in request.form:
		request_data["label_en"] = request.form["label_en"]

	if "desc_tk" in request.form:
		request_data["desc_tk"] = request.form["desc_tk"]
	if "desc_ru" in request.form:
		request_data["desc_ru"] = request.form["desc_ru"]
	if "desc_en" in request.form:
		request_data["desc_en"] = request.form["desc_en"]

	if "html_tk" in request.form:
		request_data["html_tk"] = request.form["html_tk"]
	if "html_ru" in request.form:
		request_data["html_ru"] = request.form["html_ru"]
	if "html_en" in request.form:
		request_data["html_en"] = request.form["html_en"]

	if "note_tk" in request.form:
		request_data["note_tk"] = request.form["note_tk"]
	if "note_ru" in request.form:
		request_data["note_ru"] = request.form["note_ru"]
	if "note_en" in request.form:
		request_data["note_en"] = request.form["note_en"]

	if "link" in request.form:
		request_data["link"] = request.form["link"]

	if data_type == "contacts":
		if "phone_number" in request.form:
			request_data["phone_number"] = request.form["phone_number"]

		if "home_phone_number" in request.form:
			request_data["home_phone_number"] = request.form["home_phone_number"]

		if "work_phone_number" in request.form:
			request_data["work_phone_number"] = request.form["work_phone_number"]

		if "phone_number_1" in request.form:
			request_data["phone_number_1"] = request.form["phone_number_1"]

		if "phone_number_2" in request.form:
			request_data["phone_number_2"] = request.form["phone_number_2"]

		if "phone_number_3" in request.form:
			request_data["phone_number_3"] = request.form["phone_number_3"]

		if "mail" in request.form:
			request_data["mail"] = request.form["mail"]

		if "mail_1" in request.form:
			request_data["mail_1"] = request.form["mail_1"]

		if "mail_2" in request.form:
			request_data["mail_2"] = request.form["mail_2"]

		if "mail_3" in request.form:
			request_data["mail_3"] = request.form["mail_3"]

		if "address" in request.form:
			request_data["address"] = request.form["address"]

		if "address_1" in request.form:
			request_data["address_1"] = request.form["address_1"]

		if "address_2" in request.form:
			request_data["address_2"] = request.form["address_2"]

		if "address_3" in request.form:
			request_data["address_3"] = request.form["address_3"]

		if "social_1_name" in request.form:
			request_data["social_1_name"] = request.form["social_1_name"]

		if "social_1" in request.form:
			request_data["social_1"] = request.form["social_1"]

		if "social_2_name" in request.form:
			request_data["social_2_name"] = request.form["social_2_name"]

		if "social_2" in request.form:
			request_data["social_2"] = request.form["social_2"]

		if "social_3_name" in request.form:
			request_data["social_3_name"] = request.form["social_3_name"]

		if "social_3" in request.form:
			request_data["social_3"] = request.form["social_3"]

	if data_type == "images":
		if "image" in request.files:
			file = request.files["image"]
			if len(file.filename) > 2:
				file_db_url = os.path.join(Config.UPLOAD_FOLDER, file.filename)
				file_location = os.path.join(os.path.abspath(''), 'main/static/', file_db_url)
				file.save(file_location)
				request_data["file_path"] = os.path.join('/static',file_db_url)

	return request_data