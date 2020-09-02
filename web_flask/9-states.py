#!/usr/bin/python3
""" States """
from flask import Flask
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ Close storage after each request """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ Return a page of alphabetically ordered states """
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)

    from flask import render_template
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """ Returns a page of all cities belonging to a state """
    from flask import render_template
    key = "State." + id
    if key in storage.all().keys():
        return render_template('9-states.html', state=storage.all()[key])
    else:
        return render_template('9-states.html', state=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
