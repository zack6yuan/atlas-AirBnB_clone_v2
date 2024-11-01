#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<n:int>', strict_slashes=False)
def number(n):
        return ("{} is a number".format(n))
# Error - the converter n does not exist.


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)