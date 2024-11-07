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


""" States route """
@app.route('/states', strict_slashes=False)
def states():
    """ Method: display an HTML page inside the tag BODY """
    states = storage.all(State)
    return render_template("9-states.html", states=states)
 

""" States id route """
@app.route('/states/<id>', strict_slashes=False)
def states_id():
    """ Method: display an HTML page inside the tag BODY """
    return render_template("9-states.html", states=states)


""" Method: Start Flask web server """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)