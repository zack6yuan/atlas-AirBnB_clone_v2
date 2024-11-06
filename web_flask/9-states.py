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


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State)
    return render_template("9-states.html", states=states)
 

@app.route('/states/<id>', strict_slashes=False)
def states_id():
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)