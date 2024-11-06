#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)

""" Root route """
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")

""" HBNB route """
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ("HBNB")

""" Dynamic route - captures value from URL """
@app.route('/c/<text>', strict_slashes=False)
def display(text):
    return ("C {}".format(text.replace("_", " ")))

""" Dynamic route - captures value from URL """
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    return ("Python {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
