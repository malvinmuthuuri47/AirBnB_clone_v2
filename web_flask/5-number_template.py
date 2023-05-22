#!/usr/bin/python3
"""A Script that starts a Flask web application"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """The root page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hnbn():
    """The HBNB page"""
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


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """Display number on page if its even"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display number on page whether its odd/even"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
