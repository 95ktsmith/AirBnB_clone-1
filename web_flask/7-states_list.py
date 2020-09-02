#!/usr/bin/python3
""" States list """
from flask import Flask
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Close storage after each request """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ Return a page of alphabetically ordered states """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    from flask import render_template
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
