import json


def get_posts_all(path):
    """Возвращает список словарей с постами"""

    with open(path, 'r', encoding="UTF-8") as file:
        python_file = json.load(file)
        return python_file


def get_comments_all(path):
    """Возвращает список словарей с комментами"""

    with open(path, 'r', encoding="UTF-8") as file:
        return json.load(file)


def get_posts_by_user(posts_data, user_name):
    """Возвращает список словарей с постами определенного пользователя.
         Вызывает ошибку ValueError если такого пользователя нет
         Возвращает пустой список, если у пользователя нет постов"""

    posts_list = []
    flag = False
    for post in posts_data:
        if user_name.lower() in post["poster_name"].lower():
            posts_list.append(post)
            flag = True
    if not flag:
        raise ValueError('Нет такого пользователя')
    return posts_list


def get_comments_by_post_id(post_data, comment_data, comment_id):
    """Возвращает список словарей с комментариями определенного поста.
         Функция вызывает ошибку ValueError если такого поста нет
         Функция вызывает ошибку TypeError если коммент вводится не integer
         Возвращает пустой список, если у поста нет комментов."""

    if type(comment_id) != int:
        raise TypeError

    comments_list = []
    flag = False
    for post in post_data:
        if comment_id == post["pk"]:
            comments_list = []
            flag = True
    for comment in comment_data:
        if comment_id == comment['post_id']:
            comments_list.append(comment)
            flag = True
    if not flag:
        raise ValueError('Нет такого поста')
    return comments_list


def search_for_posts(post_data, query):
    """Возвращает список словарей с  постами по ключевому слову"""

    posts_list = []
    for post in post_data:
        if query.strip().lower() in post["content"].strip().lower():
            posts_list.append(post)
    return posts_list


def get_post_by_pk(post_data, pk):
    """Возвращает один словарь с  постом по его идентификатору.
    Функция вызывает ошибку ValueError если такого меньше одного или
    больше количества всех словарей в изначальном списке
    Функция вызывает ошибку TypeError, если идентификатор вводится не integer"""

    if type(pk) != int:
        raise TypeError

    posts_list = []
    if pk < 1 or pk > len(post_data):
        raise ValueError

    for post in post_data:
        if pk == post["pk"]:
            posts_list.append(post)
            return posts_list
