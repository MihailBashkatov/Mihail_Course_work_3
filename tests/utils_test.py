from utils import get_posts_all, get_comments_all, get_comments_by_post_id, get_posts_by_user, get_post_by_pk
import pytest
path = "../data/posts.json"
path_comment = "../data/comments.json"


def test_get_posts_all():
    result = get_posts_all(path)
    assert type(result) == list, "JSON файл не преобразован в список"
    for item in result:
        assert type(item) == dict, "item не является словарем"
#


def test_get_comments_all():
    result = get_comments_all(path)
    assert type(result) == list, "JSON файл не преобразован в список"
    for item in result:
        assert type(item) == dict, "item не является словарем"


def test_get_posts_by_user():
    result = get_posts_all(path)
    for item in result:
        user_post_list = get_posts_by_user(result, item["poster_name"])
        assert type(user_post_list) == list, "item не является словарем"

        expected_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
        for user_post in user_post_list:
            key_list = []
            for key in user_post.keys():
                key_list.append(key)
            assert key_list == expected_keys, "ключи не совпадают"


# # #
def test_get_comments_by_post_id():
    all_comments = get_comments_all(path_comment)
    assert type(all_comments) == list, "не является словарем"

    expected_keys = ["post_id", "commenter_name", "comment", "pk"]
    for comment in all_comments:
        key_list = []
        for key in comment.keys():
            key_list.append(key)
        assert key_list == expected_keys, "ключи не совпадают"


#
def test_get_comments_by_post_id_error():
    post_data = get_posts_all(path)
    comment_data = get_comments_all(path_comment)
    comment_data_len = len(comment_data)
    pk = comment_data_len + 1

    with pytest.raises(ValueError):
        get_comments_by_post_id(post_data, comment_data, pk)

    with pytest.raises(TypeError):
        get_comments_by_post_id(post_data, comment_data, ['', {}, ()])


def test_get_post_by_pk():
    post_data = get_posts_all(path)
    data_len = len(post_data)
    for pk in range(1, data_len + 1):
        post_by_pk = get_post_by_pk(post_data, pk)
        assert type(post_by_pk) == list, "Возвращается не список"


def test_get_post_by_pk_error():
    post_data = get_posts_all(path)
    data_len = len(post_data)
    pk = data_len + 1

    with pytest.raises(ValueError):
        get_post_by_pk(post_data, pk)

    with pytest.raises(TypeError):
        get_post_by_pk(post_data, ['', {}, ()])
