#!/usr/bin/python3
""" Module that starts a Flask web application """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():