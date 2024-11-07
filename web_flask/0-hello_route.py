#!/usr/bin/python3
""" Method: Start a Flask web application """
from flask import Flask


app = Flask(__name__)


""" Root route """
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Method: Display "Hello HBNB!" to the user """
    return ("Hello HBNB!")


""" Method: Start Flask web server"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
