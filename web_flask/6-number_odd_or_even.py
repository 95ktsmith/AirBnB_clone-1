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


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_number_template(n):
    from flask import render_template
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_odd_even(n):
    from flask import render_template
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, text="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, text="odd")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
