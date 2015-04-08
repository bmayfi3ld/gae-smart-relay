import os
import json
import datetime

from flask import Flask
from flask import request, redirect, url_for, render_template
from google.appengine.ext import ndb
from google.appengine.api import users


app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

class Test_Entity(ndb.Model):
	property1 = ndb.StringProperty()
	property2 = ndb.StringProperty()
	
class Log(ndb.Model):
	timestamp = ndb.DateTimeProperty()
	temperature = ndb.FloatProperty()
	current = ndb.FloatProperty()
	humidity = ndb.FloatProperty()
	battery_voltage = ndb.FloatProperty()
	voltage = ndb.FloatProperty()
	frequency = ndb.FloatProperty()
	
	
@app.route('/')
def reroute():
	return redirect(url_for('data'))

@app.route('/data')
def data():
	logs = Log.query(ancestor=ndb.Key('Log', "Beaglebone1")).order(Log.timestamp)
	
	data_table = [['Time','Temperature','Humidity']]
	
	for log in logs:
		data_table.append([log.timestamp.ctime(), log.temperature, log.humidity])

		
	return render_template('index.html', data_table = data_table)

@app.route('/post')
def post():
	new_log = Log(parent=ndb.Key('Log', "Beaglebone1"))
	# try:
	string_time = request.args.get('timestamp')
	new_log.timestamp = datetime.datetime.fromtimestamp(float(string_time))
	new_log.temperature = float(request.args.get('temperature'))
	new_log.current = request.args.get('current')
	new_log.humidity = float(request.args.get('humidity'))
	new_log.battery_voltage = request.args.get('battery_voltage')
	new_log.voltage = request.args.get('voltage')
	new_log.frequency = request.args.get('frequency')
	password = request.args.get('password')
	# except:
		# return 'failure'
	if password == 'my_password':
		new_log.put()
		return 'success'
	else:
		return 'failure'
	
@app.route('/control')
def control():
	user = users.get_current_user()
	
	if user:
		name = user.nickname()
	else:
		return redirect(users.create_login_url())
		
	return render_template('control.html', user = name)
	
@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
