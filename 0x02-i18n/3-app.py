#!/usr/bin/env python3
"""flask app"""
from flask import (
        Flask,
        render_template,
        request
)
from flask_babel import Babel


class Config(object):
    """babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFUALT_LOCALE = "en",
    BABEL_DEFAULT_TIMEZONE = "UFC"



app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)



app.jinja_env.autoescape = True



@babel.localeselector
def get_locale():
    """return best language match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """app route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
