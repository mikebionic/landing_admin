
from main.web import bp

@bp.route("/hello")
def hello():
	return "Hello world"