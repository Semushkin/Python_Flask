from flask import Blueprint, render_template

main = Blueprint('main_page', __name__, url_prefix='/', static_folder='../static')


@main.route('/')
def main_page():
    return render_template('main_page/main_page.html')

