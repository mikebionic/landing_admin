# -*- coding: utf-8 -*-
from flask import Flask,session,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_babel import Babel,format_date,gettext,lazy_gettext
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_caching import Cache
from flask_compress import Compress
import logging
from htmlmin.main import minify

from main.config import Config


babel = Babel()
db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()
csrf = CSRFProtect()
cache = Cache()
compress = Compress()

login_manager.login_view = 'web.home'
login_manager.login_message = lazy_gettext('Login the system!')
login_manager.login_message_category = 'info'


@babel.localeselector
def get_locale():
	language = Config.BABEL_DEFAULT_LOCALE
	if 'language' in session:
		language = session['language'] if session['language'] else Config.BABEL_DEFAULT_LOCALE
	return language

def create_app(config_class=Config):
	app = Flask(__name__, static_url_path=Config.STATIC_URL_PATH)
	app.config.from_object(Config)
	app.static_folder = Config.STATIC_FOLDER_LOCATION
	app.template_folder = Config.TEMPLATE_FOLDER_LOCATION
	if Config.USE_FLASK_CORS:
		CORS(app, supports_credentials=True)
	
	print(app.config['SECRET_KEY'])

	db.init_app(app)
	login_manager.init_app(app)
	babel.init_app(app)
	csrf.init_app(app)
	cache.init_app(app)

	if Config.USE_FLASK_COMPRESS:
		compress.init_app(app)

	if Config.OS_TYPE != 'win32':
		sess.init_app(app)
	
	api_url_prefix = Config.API_URL_PREFIX
	web_url_prefix = Config.WEB_URL_PREFIX
	admin_url_prefix = Config.ADMIN_URL_PREFIX

	from . import models
	
	from main.admin import bp as admin_bp
	app.register_blueprint(admin_bp, url_prefix=f"{admin_url_prefix}/")
	csrf.exempt(admin_bp)

	from main.web import bp as web_bp
	app.register_blueprint(web_bp, url_prefix=f"{web_url_prefix}/")
	csrf.exempt(web_bp)


	@app.route("/set_language/<code>")
	def set_language(code):
		session['language'] = code
		return redirect(url_for('web.home'))

	@app.after_request
	def response_minify(response):
		if Config.MINIFY_HTML_RESPONSE:
			if response.content_type == u'text/html; charset=utf-8':
				response.set_data(minify(response.get_data(as_text=True)))
		return response

	return app