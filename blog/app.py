from time import time

from flask import Flask, request, g
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
from blog.models import User
from blog.extentions import login_manager, db, migrate, csrf
from blog import commands


# db = SQLAlchemy()
# login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
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


def register_extensions(app):

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
