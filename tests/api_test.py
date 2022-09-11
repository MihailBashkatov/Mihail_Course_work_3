# Импорт необходимых библиотек и функций
from run import app
from utils import get_posts_all

# Определение пути файла с данными
path = "data/posts.json"


def test_api_blueprint():
    """ Тест на возврат загруженного файла в формате списка"""

    response = app.test_client().get("/api/posts/")
    assert type(response.json) == list, "Должен возвращаться список"


def test_api_blueprint_elements():
    """Тест на тип элемента списка - словарь"""
    response = app.test_client().get("/api/posts/")
    for element in response.json:
        assert type(element) == dict, "Должен возвращаться словарь"


def test_api_blueprint_keys():
    """ Тест на соответствие ключей и значений всех элементов списка"""
    response = app.test_client().get("/api/posts/")
    for element in response.json:
        for key, value in element.items():

            assert element[key] == value, "ключ не соответствует значению"


def test_api_blueprint_postid():
    """Тест на тип элемента списка - словарь"""

    posts = get_posts_all(path)
    for index in range(len(posts)):
        response = app.test_client().get(f"/api/posts/{index + 1}")
        assert type(response.json) == list, "Должен возвращаться словарь"


def test_api_blueprint_postid_keys():
    """ Тест на соответствие ключей и значений элемента списка"""

    posts = get_posts_all(path)
    for index in range(len(posts)):
        response = app.test_client().get(f"/api/posts/{index + 1}")
        for element in response.json:
            for key, value in element.items():
                assert element[key] == value, "ключ не соответствует значению"
