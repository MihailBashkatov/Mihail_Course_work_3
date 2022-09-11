# Импорт необходимых библиотек и функций
from flask import render_template, Blueprint
from utils import get_posts_all

# Создание эскиза
main_blueprint = Blueprint("main_blueprint ", __name__, template_folder="templates_main", static_folder="static_main")

# Определение пути файла с данными
posts = "data/posts.json"


@main_blueprint.route('/')
def main_page():
    """ Представление основной страницы"""

    all_posts = get_posts_all(posts)
    return render_template("index.html", all_posts=all_posts)


@main_blueprint.errorhandler(404)
def page_not_found(e):
    """ Представление страницы с ошибкой 404"""

    return render_template("404.html"), 404


@main_blueprint.errorhandler(500)
def internal_server_error(e):
    """ Представление страницы с ошибкой 505"""

    return render_template('500.html'), 500
