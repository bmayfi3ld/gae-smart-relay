import os
import json

from flask import Flask
from flask import request, redirect, url_for, render_template
from google.appengine.ext import ndb

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class Test_Entity(ndb.Model):
	property1 = ndb.StringProperty()
	property2 = ndb.StringProperty()
	
	
@app.route('/')
def reroute():
	return redirect(url_for('data'))

@app.route('/data')
def data():
	the_list = '<b>Hello World!</b>' 
	tests = Test_Entity.query(ancestor=ndb.Key('Test_Entity', "MasterKey"))
	json.dumps('\\')
	
	data_table = [
	['time','first','second','third'],
	[1,  37.8, 80.8, 41.8],
	[2,  30.9, 69.5, 32.4],
	[3,  25.4,   57, 25.7],
	[4,  11.7, 18.8, 10.5],
	[5,  11.9, 17.6, 10.4],
	[6,   8.8, 13.6,  7.7],
	[7,   7.6, 12.3,  9.6],
	[8,  12.3, 29.2, 10.6],
	[9,  16.9, 42.9, 14.8],
	[10, 12.8, 30.9, 11.6],
	[11,  5.3,  7.9,  4.7],
	[12,  6.6,  8.4,  5.2],
	[13,  4.8,  6.3,  3.6],
	[14,  4.2,  6.2,  3.4]
    ]
	
	for test in tests:
		the_list += '<p>'
		the_list += test.property1
		the_list += '</p>'
		
	return render_template('index.html', the_list = the_list, data_table = json.dumps(data_table))

@app.route('/post')
def post():
	new_test_entity = Test_Entity(parent=ndb.Key('Test_Entity', "MasterKey"))
	new_test_entity.property1 = request.args.get('p1')
	new_test_entity.property2 = request.args.get('p2')
	new_test_entity.put()
	return redirect(url_for('hello'))
	
@app.route('/control')
def control():
	return 'This page is not done yet'
	
@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
