from flask import Blueprint, render_template, redirect
from blog.user.views import USERS
import copy

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Article 1',
        'text': 'article 1 text',
        'author': 1
    },
    2: {
        'title': 'Article 2',
        'text': 'article 2 text',
        'author': 2
    },
    3: {
        'title': 'Article 3',
        'text': 'article 3 text',
        'author': 3
    }
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article = copy.copy(ARTICLES[pk])
    except KeyError:
        return redirect('/articles/')
    # article['author'] = USERS[article['author']]
    return render_template(
        'articles/details.html',
        article=article,
        user_name=USERS[article['author']]
        # user=USERS[article['author']]
        )
