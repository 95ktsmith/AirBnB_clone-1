#!/usr/bin/python3
""" HBNB Route """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Hello hbnb """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
