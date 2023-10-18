#!/usr/bin/python3
"""app with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string 
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string 
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted 
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat  based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)i
