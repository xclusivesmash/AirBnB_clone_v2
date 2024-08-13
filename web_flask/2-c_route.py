#!/usr/bin/python3
"""
Module: 2-c_route
Description: using more routes.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns a simple message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world():
    """Extention of the firts route."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Displays the given text."""
    string = f"C {text}"
    return string.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
