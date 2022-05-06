
import sys, redis, json
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath('.')
load_dotenv(path.join(basedir, '.env'))

class Config:
	OS_TYPE = sys.platform
	APP_BASEDIR = path.abspath('.')
	APP_PORT = int(environ.get('APP_PORT')) if environ.get('APP_PORT') else 5000
	APP_HOST = environ.get('APP_HOST') or "0.0.0.0"

	SECRET_KEY = environ.get('SECRET_KEY') or 'secret'
	FLASK_ENV = 'development'
	DEBUG = int(environ.get('DEBUG')) if environ.get('DEBUG') else 1
	TESTING = int(environ.get('TESTING')) if environ.get('TESTING') else 1

	USE_FLASK_CORS = int(environ.get('USE_FLASK_CORS')) if environ.get('USE_FLASK_CORS') else 1
	CORS_EXEMPT_SSR_ROUTES = int(environ.get('CORS_EXEMPT_SSR_ROUTES')) if environ.get('CORS_EXEMPT_SSR_ROUTES') else 0
	USE_FLASK_COMPRESS = int(environ.get('USE_FLASK_COMPRESS')) if environ.get('USE_FLASK_COMPRESS') else 1
	COMPRESS_LEVEL = 6
	MINIFY_HTML_RESPONSE = int(environ.get('MINIFY_HTML_RESPONSE')) if environ.get('MINIFY_HTML_RESPONSE') else 1


	if OS_TYPE != 'win32':
		SESSION_TYPE = environ.get('SESSION_TYPE')
		SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS')) if environ.get('SESSION_REDIS') else redis.from_url('redis://:@127.0.0.1:6379/1')
	CACHE_TYPE = environ.get('CACHE_TYPE') or ''
	CACHE_DEFAULT_TIMEOUT = 300
	DB_CACHE_TIME = int(environ.get('DB_CACHE_TIME')) if environ.get('DB_CACHE_TIME') else 600
	CACHE_REDIS_URL = environ.get('CACHE_REDIS_URL') or 'redis://:@127.0.0.1:6379/2'

	COMPANY_NAME = environ.get('COMPANY_NAME') or 'Company'
	COMPANY_MAIL = environ.get('COMPANY_MAIL') or 'company@mail.com'


	STATIC_FOLDER_PATH = path.join(*json.loads(environ.get('STATIC_FOLDER_PATH'))) if environ.get('STATIC_FOLDER_PATH') else path.join('main','static')
	STATIC_FOLDER_LOCATION = path.join(APP_BASEDIR, STATIC_FOLDER_PATH)
	STATIC_URL_PATH = environ.get('STATIC_URL_PATH') if environ.get('STATIC_URL_PATH') else '/app/static'
	TEMPLATE_FOLDER_PATH = path.join(*json.loads(environ.get('TEMPLATE_FOLDER_PATH'))) if environ.get('TEMPLATE_FOLDER_PATH') else path.join('main','templates')
	TEMPLATE_FOLDER_LOCATION = path.join(APP_BASEDIR, TEMPLATE_FOLDER_PATH)

	# SQLALCHEMY_DATABASE_URI = 'sqlite:///commerce.db'

	DB_TYPE = environ.get('DB_TYPE') or 'postgres'
	DB_URI_DATA = {
		'user': environ.get('DB_USERNAME'),
		'pw': environ.get('DB_PASSWORD'),
		'db': environ.get('DB_DATABASE'),
		'host': environ.get('DB_HOST'),
		'port': environ.get('DB_PORT'),
		'driver': environ.get('DB_DRIVER') or '',
		'additionalFields': environ.get('DB_ADDITIONAL_FIELDS') or ''
	}
	if DB_TYPE.lower() == "mssql":
		SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s?driver=%(driver)s%(additionalFields)s" % DB_URI_DATA

	if DB_TYPE.lower() == "postgres":
		SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s%(additionalFields)s' % DB_URI_DATA
	
	SQLALCHEMY_ECHO = int(environ.get('SQLALCHEMY_ECHO')) if environ.get('SQLALCHEMY_ECHO') else 0

	API_URL_PREFIX = environ.get('API_URL_PREFIX') or '/api'
	WEB_URL_PREFIX = environ.get('WEB_URL_PREFIX') or ''
	ADMIN_URL_PREFIX = environ.get('ADMIN_URL_PREFIX') or ''
	BABEL_DEFAULT_LOCALE = environ.get('BABEL_DEFAULT_LOCALE') or 'tk'

	TOKEN_EXP_TIME_MINUTES = int(environ.get('TOKEN_EXP_TIME_MINUTES')) if environ.get('TOKEN_EXP_TIME_MINUTES') else 30
	JWT_ALGORITHM = environ.get('JWT_ALGORITHM') or "HS256"
	FILENAME_INVALID_CHARACTERS = ['/', '\\', '"', ':', '*', '?', '<', '>', '|']
	BLOB_TO_IMAGE_SAVE_EXT = "png"
	UPLOAD_FOLDER = "uploads"


	WEB_CONFIG_DIRECTORY = path.join("web_config")
	GOOGLE_ANALYTICS_TAG = environ.get('GOOGLE_ANALYTICS_TAG') or ''
	HOME_PAGE_TITLE = environ.get('HOME_PAGE_TITLE') or "Welcome!"
	WEB_TEMPLATE_FOLDER = environ.get('WEB_TEMPLATE_FOLDER') or 'web/index.html'