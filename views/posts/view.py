# Импорт необходимых библиотек и функций
from flask import Blueprint, render_template
from utils import get_post_by_pk, get_comments_by_post_id, get_posts_all, get_comments_all

# Определение пути файла с данными
PATH_POSTS = "data/posts.json"
PATH_COMMENTS = "data/comments.json"

# Создание эскиза
post_blueprint = Blueprint("post_blueprint", __name__, template_folder="templates_posts", static_folder="static_posts")


@post_blueprint.route('/posts/<int:postid>')
def get_posts(postid):
    """ Представление  страницы по номеру поста"""

    try:
        posts = get_posts_all(PATH_POSTS)
        comments = get_comments_all(PATH_COMMENTS)
        posts_by_pk = get_post_by_pk(posts, postid)
        comments_by_pk = get_comments_by_post_id(posts, comments, postid)
        comments_len = len(comments)
        return render_template("post.html", posts_by_pk=posts_by_pk, comments_by_pk=comments_by_pk,
                               comments_len=comments_len)
    except ValueError:
        return "Информация не найдена"


@post_blueprint.errorhandler(404)
def page_not_found(e):
    """ Представление страницы с ошибкой 404"""

    return render_template("404.html"), 404


@post_blueprint.errorhandler(500)
def internal_server_error(e):
    """ Представление страницы с ошибкой 505"""

    return render_template('500.html'), 500
