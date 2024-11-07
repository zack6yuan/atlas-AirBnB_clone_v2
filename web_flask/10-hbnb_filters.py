#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


""" HBNB filters route """
@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    state = storage.all(State).values()
    amenity = storage.all(State).values()
    return render_template("10-hbnb_filters.html", state=state, amenity=amenity)


""" TearDown """
@app.teardown_appcontext
def teardown():
    """ Method: Remove the current SQLAlchemy session """
    storage.close()


""" Method: Start Flask web server """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)