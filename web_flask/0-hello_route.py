#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)


""" Method: Root route """
@app.route('/', strict_slashes=False)
def hello():
    """ Method: Display "Hello HBNB!" to the user """
    return ("Hello HBNB!")


""" Method: Start Flask web server"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
