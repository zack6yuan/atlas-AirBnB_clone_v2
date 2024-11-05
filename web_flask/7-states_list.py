#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Method: Remove the current SQLAlchemy session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    
    return render_template('7-states_list.html', n=n)