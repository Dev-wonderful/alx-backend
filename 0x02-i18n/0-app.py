#!/usr/bin/env python3
"""A simple flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Index route for the app"""
    return render_template("0-index.html")


app.run("127.0.0.1", 5000, debug=True)
