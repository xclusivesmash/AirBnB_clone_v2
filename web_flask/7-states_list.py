#!/usr/bin/python3
"""
Module: 7-states_list
Description: more app routes added.
"""
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """render an HTML page"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
