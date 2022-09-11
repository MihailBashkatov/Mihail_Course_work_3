# Импорт необходимых библиотек и функций
from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk
import logging

# Создание эскиза
api_blueprint = Blueprint("api_blueprint", __name__)

# Определение пути файла с данными
PATH = "data/posts.json"

# # Создание файла и уровня лога
logging.basicConfig(level='WARNING', format='%(asctime)s : [%(levelname)s] : %(message)s', filename="api.log")


@api_blueprint.route('/api/posts/', methods=['GET'])
def posts_json():
    """ Представление  страницы, со всеми загруженными постами в формате JSON"""

    logging.warning("Запрос/api/posts")
    posts_all = get_posts_all(PATH)
    return jsonify(posts_all)


@api_blueprint.route('/api/posts/<int:post_id>', methods=['GET'])
def single_post_json_(post_id):
    """ Представление  страницы, с конкретным  постам в формате JSON"""

    posts = get_posts_all(PATH)
    post_by_pk = get_post_by_pk(posts, post_id)
    logging.warning(f"Запрос /api/posts/{post_id}")
    return jsonify(post_by_pk)
