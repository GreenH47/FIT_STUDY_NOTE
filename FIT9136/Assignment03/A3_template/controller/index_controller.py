from flask import render_template, Blueprint

from model.user import User
from model.user_admin import Admin

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():
    context = {}
    # check the class variable User.current_login_user
    if User.current_login_user:
        context['current_user_role'] = User.current_login_user.role
    # manually register an admin account when open index page
    if not User().check_username_exist('admin'):
        Admin().register_admin()
    return render_template("01index.html", **context)
