
from main.web import bp

@bp.route("/")
@bp.route("/home")
def home():
	return "home world"