from flask_login import UserMixin

from blog.app import db
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))


# class Article(db.Model):
#     __tablename__ = 'Article'
#
#     title = db.Column(db.String(255))
#     text = db.Column(db.String)
#     author = relationship('User')

