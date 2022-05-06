

def add_data_from_form(request, data_type=None):
	request_data = {}
	if "name" in request.form:
		request_data["name"] = request.form["name"]
	if "title" in request.form:
		request_data["title"] = request.form["title"]
	if "label" in request.form:
		request_data["label"] = request.form["label"]
	if "desc" in request.form:
		request_data["desc"] = request.form["desc"]
	if "html" in request.form:
		request_data["html"] = request.form["html"]

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


	return request_data
