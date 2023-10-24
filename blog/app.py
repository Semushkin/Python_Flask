from time import time

from flask import Flask, request, g

from blog.article.views import article
from blog.user.views import user
from blog.main.views import main


# app = Flask(__name__)
#
#
# @app.route('/<string:city>')
# def index(city: str):
#     return f'Hello! {city}'
#
#
# @app.before_request
# def process_before_request():
#     g.start_time = time()
#
#
# @app.after_request
# def process_after_request(response):
#     if hasattr(g, 'start_time'):
#         response.headers['process-time'] = time() - g.start_time
#
#     return response
#
#
# @app.errorhandler(404)
# def handler_404(error):
#     app.logger.error(error)
#     return '404'


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(main)
