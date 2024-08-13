#!/usr/bin/python3
"""
Module: 4-number_route
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


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_print(text):
    """Prints a text based on input."""
    string = f"Python {text}"
    return string.replace("_", " ")


@app.route("/number/<int:n>")
def display_n(n):
    """Displays n if only integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
