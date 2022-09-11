# Импорт библиотеки flask
from flask import Flask
import logging

# Импорт блюпринтов
from views.main.view import main_blueprint
from views.search.view import search_blueprint
from views.posts.view import post_blueprint
from views.api.view import api_blueprint


# Объявление экземпляра класса Flask
app = Flask(__name__)

# Распознавание кириллицы
app.config['JSON_AS_ASCII'] = False

# Регистрация  блюпринтов
app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(port=18920)
