from flask import redirect, render_template, request, url_for, flash
from flask_login import login_user, current_user, logout_user

from . import bp
from main.models import User



@bp.route('/logout/')
def admin_logout():
	logout_user()
	return redirect(url_for('web.home'))

@bp.route('/login/', methods=["GET","POST"])
def admin_login():
	message = "Please login"
	if current_user.is_authenticated:		
		return redirect(url_for('admin.dashboard'))

	if request.method == "POST":
		try:
			username = request.form["username"]
			password = request.form["password"]
			print(username, password)
			if not username or not password:
				message = "Bad credentials"
				raise Exception

			admin_user = User.query.filter_by(
				username = username,
				password = password,
				type_id = 1,
			).first()

			if not admin_user:
				message = "Wrong credentials"
				raise Exception

			login_user(admin_user)
			return redirect(url_for('admin.dashboard'))

		except Exception as e:
			flash(message)
			print(f"admin login exception: {e}")

	return render_template("admin/login.html", message=message)