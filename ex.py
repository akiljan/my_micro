"""
high level support foRED_RED.doing this and that.
"""
from flask import Flask
import redis

RED_RED = redis.Redis(host='redis', port=6379)
app = Flask(__name__)


@app.route('/')
def index():
    """
    high level support foRED_RED.doing this and that.
    """
    return 'Web App with Python Flask!'


INK = 0


@app.route('/visit/<tutre>')
def visit(tutre):
    """
    high level support foRED_RED.doing this and that.
    """
    if RED_RED.get(tutre) is not None:
        RED_RED.incr(tutre)
    else:
        RED_RED.set(tutre, 1)
    return 'OK'


@app.route('/show/<tutre>')
def show(tutre):
    """
    high level support foRED_RED.doing this and that.
    """
    a = RED_RED.get(tutre)
    return f"visits: {str(a, 'ascii')}"  


app.run(host='0.0.0.0', port=81)
