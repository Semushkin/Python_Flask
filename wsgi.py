from blog.app import create_app
from blog.extentions import db

from werkzeug.security import generate_password_hash

# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         debug=True,
#     )

app = create_app()
app.run()


# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#
#
# @app.cli.command('create-users')
# def create_users():
#     from blog.models import User
#
#     db.session.add(
#         User(username='Ivan', password=generate_password_hash('test123'))
#     )
#     db.session.commit()
