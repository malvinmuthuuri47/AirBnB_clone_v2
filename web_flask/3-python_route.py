#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """The home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hnbn():
    """The hbnb page"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """The C page"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def hello_python(text="is cool"):
    """The Python page"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
