#!/usr/bin/python3
"""
Module: 5-number_template
Description: using more routes.
"""
from flask import Flask


app = Flask(__name__, template_folder="templates")


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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp(n):
    """Displays n inside ahtml h1 tag"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
