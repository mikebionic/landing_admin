from flask import Blueprint

from main.config import Config

bp = Blueprint('admin',__name__)
url_prefix = Config.ADMIN_URL_PREFIX

from . import (
	auth,
	routes,
)