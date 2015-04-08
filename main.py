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

class BB_Status(ndb.Model):
	state = ndb.BooleanProperty()
	command = ndb.BooleanProperty()
	
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

	# create entities
	new_log = Log(parent=ndb.Key('Log', "Beaglebone1"))
	status_key = ndb.Key(BB_Status, 'Beaglebone1')
	status = status_key.get()
	
	if not status:
		status = BB_Status(key=status_key)
	
	# fill data
	string_time = request.args.get('timestamp')
	new_log.timestamp = datetime.datetime.fromtimestamp(float(string_time))
	new_log.temperature = float(request.args.get('temperature'))
	new_log.current = request.args.get('current')
	new_log.humidity = float(request.args.get('humidity'))
	new_log.battery_voltage = request.args.get('battery_voltage')
	new_log.voltage = request.args.get('voltage')
	new_log.frequency = request.args.get('frequency')
	password = request.args.get('password')
	
	if request.args.get('state') == 'True':
		status.state = True
	else:
		status.state = False
		
	# save data
	if password == 'my_password':
		new_log.put()
		status.put()
		return 'success'
	else:
		return 'failure'
	
@app.route('/control')
def control():
	user = users.get_current_user()
	
	if not user:
		return redirect(users.create_login_url())

	status_key = ndb.Key(BB_Status, 'Beaglebone1')
	status = status_key.get()
	
	return render_template('control.html', state = status.state)
	
@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
