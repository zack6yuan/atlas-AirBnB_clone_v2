#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)

""" Method: Root route """
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Method: Display "Hello HBNB!" to the user """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Method: Display "HBNB" to the user """
    return ("HBNB")


""" Method: Start Flask web server"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
