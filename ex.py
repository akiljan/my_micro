"""
high level support for doing this and that.
"""
from flask import Flask
import redis

r = redis.Redis(host='redis', port=6379)
app = Flask(__name__)


@app.route('/')

def index():
    """
    high level support for doing this and that.
    """
    return 'Web App with Python Flask!'


ink = 0


@app.route('/visit/<tutre>')
def visit(tutre):
    """
    high level support for doing this and that.
    """
    if r.get(tutre) is not None:
        r.incr(tutre)
    else:
        r.set(tutre, 1)

    return 'OK'


@app.route('/show/<tutre>')
def show(tutre):
    """
    high level support for doing this and that.
    """
    a = r.get(tutre)
    return "visits: %s" % str(a, 'ascii')


app.run(host='0.0.0.0', port=81)
