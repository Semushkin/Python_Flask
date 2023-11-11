from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ForeignKey

# from blog.app import db
from sqlalchemy.orm import relationship
from blog.extentions import db


class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, default='', server_default='')

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Author(db.Model):
    __tablename__ = 'Author'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('User.id'), nullable=False)

    user = relationship('User', back_populates='author')
    article = relationship('Article', back_populates='author')


class Article(db.Model):
    __tablename__ = 'Article'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('Author.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='article')
