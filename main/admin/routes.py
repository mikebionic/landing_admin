from flask import render_template
from flask_login import login_required

from . import bp

@bp.route("/dashboard/")
@login_required
def dashboard():
	return "Hello, it's dashboard"