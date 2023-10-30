from time import time

from flask import Flask, request, g
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from blog.models import User


db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8#5%-!wy+^55ov4nm)7v@x7z1*odvt_$tphd()&qji2*w@ob4w'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # from .models import User
    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.article.views import article
    from blog.auth.views import auth
    from blog.user.views import user
    from blog.main.views import main

    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(main)
    app.register_blueprint(auth)
