from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

# from blog.app import login_manager

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

# USERS = ['Alice', 'Jon', 'Mike']
USERS = {
    1: 'Alice',
    2: 'Jon',
    3: 'Mike',
}


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
# @login_manager.user_loader
@login_required
def get_user(pk: int):
    from blog.models import User
    user = User.query.filter_by(id=pk).one_or_none()
    if not user:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template(
        'users/details.html',
        user=user,
    )
