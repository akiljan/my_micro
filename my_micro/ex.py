from flask import Flask
import redis
r=redis.Redis(host='redis', port=6379)
app = Flask(__name__)

@app.route('/')
def index():
	return 'Web App with Python Flask!'
ink=0
@app.route('/visit/<id>')

def visit(id):
	if r.get(id) is not None:
		r.incr(id)
	else:
		r.set(id,1)
	
	return 'OK'
@app.route('/show/<id>')
def show(id):
	a=r.get(id)
	return "visits: %s" % str(a, 'ascii')
app.run(host='0.0.0.0', port=81)
