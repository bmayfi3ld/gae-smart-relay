
from flask import Flask
from flask import request,redirect, url_for
from google.appengine.ext import ndb

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class Test_Entity(ndb.Model):
	property1 = ndb.StringProperty()
	property2 = ndb.StringProperty()

@app.route('/')
def hello():
	"""Return a friendly HTTP greeting."""
	return_string = '<b>Hello World!</b>' 
	tests = Test_Entity.query(ancestor=ndb.Key('Test_Entity', "MasterKey"))
	
	for test in tests:
		return_string += '<p>'
		return_string += test.property1
		return_string += '</p>'
	
	return return_string

@app.route('/post')
def post():
	new_test_entity = Test_Entity(parent=ndb.Key('Test_Entity', "MasterKey"))
	new_test_entity.property1 = request.args.get('p1')
	new_test_entity.property2 = request.args.get('p2')
	new_test_entity.put()
	return redirect(url_for('hello'))
	
	
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
