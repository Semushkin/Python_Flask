from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash

from blog.forms.user import UserLoginForm

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['POST', 'GET'])
def login():

    form = UserLoginForm(request.form)
    if request.method == 'GET':
        return render_template(
            'auth/login.html',
            form=form
        )

    # username = request.form.get('username')
    # password = request.form.get('password')
    username = form.username.data
    password = form.password.data

    from blog.models import User

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return render_template('auth/login.html', form=form, errors=['Check your login details',])

    login_user(user)
    return redirect(url_for('user.get_user', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
