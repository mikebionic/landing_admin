# -*- coding: utf-8 -*-
from main import create_app
from main.config import Config

app = create_app()

app_port = int(Config.APP_PORT) if Config.APP_PORT else 5000
app_host = Config.APP_HOST or "0.0.0.0"

if __name__ == "__main__":
	app.jinja_env.cache = {}
	app.run(host=app_host, port=app_port, threaded=True)