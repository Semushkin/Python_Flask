from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash

from blog.extentions import db
from blog.forms.user import UserRegisterForm
from blog.models import User

# from blog.app import login_manager

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


USERS = {
    1: 'Alice',
    2: 'Jon',
    3: 'Mike',
}


@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.get_user', pk=current_user.id))

    form = UserRegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Email not uniq')
            return render_template('users/register.html', form=form)

        _user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()
        login_user(_user)

    return render_template(
        'users/register.html',
        form=form,
    )


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
