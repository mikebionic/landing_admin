from flask import render_template

from . import bp
from main.config import Config

from .utils import get_all_data

@bp.route("/")
@bp.route("/home")
def home():
	data = get_all_data()
	print(data)
	return render_template(Config.WEB_TEMPLATE_FOLDER, data=data)