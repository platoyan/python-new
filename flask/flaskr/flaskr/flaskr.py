#all the imports
import os
import sqlite3
from flask import Flask,request, session, g, redirect, url_for, abort, render_template, flash

#The next couple lines will create the actual application instance and initialize it with the config from the same file in flaskr.py:
app = Flask(__name__) #create application instance
app.config.from_object(__name__) # load config from this file, flaskr.py
#load default config and override config from an envrionment variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path,'flaskr.db'),
	SECRECT_KEY='development key',
	USERNAME='admin',
	PASSWORD='admin'
))
app.config.from_envvar('FLASK_SETTINGS',silent=True)
def connect_db():
	"""Connects to the specific database."""
	rv = sqliqaste3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv
def get_db():
	if not hasattr(g,'sqlite.db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
	"""Closes the database again at the end of the request."""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()
def init_db():
	db=get_db()
	with app.open_resource('schema.sql',mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()
@app.cli.command('initdb')
def initdb_command():
	init_db()
	print('Initialized the database.')

