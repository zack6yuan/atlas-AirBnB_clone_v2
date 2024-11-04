#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask, render_template


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
<<<<<<< HEAD
def python(text="is cool")
=======
def python(text="is cool"):
>>>>>>> 16cf3566043d00b455a17824fbe325577649a514
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<n>', strict_slashes=False)
def template(n):
<<<<<<< HEAD
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def template(n):
    return render_template('6-number_odd_or_even.html', n=n)
=======
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def oddoreven_template(n):
    return render_template("6-number.html", number=n)
>>>>>>> 16cf3566043d00b455a17824fbe325577649a514
