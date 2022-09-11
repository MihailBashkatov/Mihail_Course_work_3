from run import app
from utils import get_posts_all

path = "data/posts.json"

def test_api_blueprint():
    response = app.test_client().get("/api/posts/")
    assert type(response.json) == list, "Должен возвращаться список"


def test_api_blueprint_elements():
    response = app.test_client().get("/api/posts/")
    for element in response.json:
        assert type(element) == dict, "Должен возвращаться словарь"


def test_api_blueprint_keys():
    response = app.test_client().get("/api/posts/")
    for element in response.json:
        for key, value in element.items():

            assert element[key] == value, "ключ не соответствует значению"


def test_api_blueprint_postid():
    posts = get_posts_all(path)
    for index in range(len(posts)):
        response = app.test_client().get(f"/api/posts/{index + 1}")
        assert type(response.json) == list, "Должен возвращаться словарь"


def test_api_blueprint_postid_keys():
    posts = get_posts_all(path)
    for index in range(len(posts)):
        response = app.test_client().get(f"/api/posts/{index + 1}")
        for element in response.json:
            for key, value in element.items():
                assert element[key] == value, "ключ не соответствует значению"
