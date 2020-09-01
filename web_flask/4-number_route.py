#!/usr/bin/python3
""" Number Route """
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


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ Hello c """
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """ Hello python """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ Hello number """
    return str(n) + " is a number"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
