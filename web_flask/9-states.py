#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Method: Remove the current SQLAlchemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
 

@app.route('/states/<id>', strict_slashes=False)