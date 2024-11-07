#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


""" TearDown """
@app.teardown_appcontext
def teardown():
    """ Method: Remove the current SQLAlchemy session """
    storage.close()


""" States list route """
@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Method: Sort all state objects """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


""" Method: Start Flask web server """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
