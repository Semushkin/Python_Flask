from blog.extentions import db
from werkzeug.security import generate_password_hash
import click


# @app.cli.command('init-db')
@click.command('init_db')
def init_db():
    from wsgi import app
    from blog.models import User
    db.create_all(app=app)


# @app.cli.command('create-users')
@click.command('create_users')
def create_users():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username='Ivan', password=generate_password_hash('test123'), email='ivan@mail.ru'),
        )
        db.session.commit()
