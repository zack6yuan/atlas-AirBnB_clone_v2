#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)


""" Root route """
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Method: Display "Hello HBNB!" to the user """
    return ("Hello HBNB!")


""" HBNB route """
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Method: Display "HBNB" to the user """
    return ("HBNB")


""" Dynamic route - captures value from URL """
@app.route("/c/<text>", strict_slashes=False)
def display(text):
    """ Method: Display "C" followed by text value """
    return ("C {}".format(text.replace("_", " ")))


""" Method: Start Flask web server"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
