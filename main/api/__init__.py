from flask import Blueprint

from main.config import Config

api = Blueprint('api',__name__)
url_prefix = Config.API_URL_PREFIX

from . import (
	routes
)