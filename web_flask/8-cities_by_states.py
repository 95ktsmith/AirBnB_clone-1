#!/usr/bin/python3
""" Cities by state list """
from flask import Flask
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Close storage after each request """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Return a page of alphabetically ordered states and cities """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    from flask import render_template
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
