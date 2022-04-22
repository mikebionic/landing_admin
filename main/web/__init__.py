from flask import Blueprint

from main.config import Config

bp = Blueprint('web',__name__)
url_prefix = Config.WEB_URL_PREFIX

from . import (
	routes
)