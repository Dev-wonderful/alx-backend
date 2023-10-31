#!/usr/bin/env python3
"""A simple flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """The config for languages in babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config())


@app.route("/")
def index():
    """Index route for the app"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 5000, debug=True)
