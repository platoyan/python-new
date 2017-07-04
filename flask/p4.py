#Routing
#@app.route("")


#Variable Rules
#<variable_name>      <converter:variable_name>
from flask import Flask,url_for
app=Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username
@app.route('/user/<path:post_id>')
def show_post(post_id):
	return 'Post %s' % post_id
#converters exist:
#string			accepts any text without a slash (the default)
#int 			accept integers
#float 			like int but for floating point values
#path 			like the default but also accepts slashes
#any			matches one of the items provided
#uuid			accepts UUID strings 

#URLs Behavior:
#There are two rules:
#the canonical URL for the projects endpoint has a trailing slash.
#accessing it without a trailing slash will cause Flask to redirect to the canonical URL with the trailing slash. 
@app.route('/projects/')
def projects():
	return 'The project page'
# Accessing the URL with a trailing slash will produce a 404 “Not Found” error
@app.route('/about')
def about():
	return 'The about page'


#URL Building:
#To build a URL to a specific function you can use the url_for() function.
@app.route('/')
def index():
	pass
@app.route('/login')
def login():
	pass
@app.route('/user/<username>')
def profile(username):
	pass
with app.test_request_context():
	#url_for() the name of the function as first argument and a number of keyword arguments
	print(url_for('index')) #/
	print(url_for('login')) #/login
	print(url_for('login',next='/')) #/login?next=%2F
	print(url_for('profile',username='John Doe')) #/user/John%20Doe


#HTTP method
from flask import request
def do_the_login():
	return 'POST'
def show_the_login_form():
	return 'GET'
@app.route('/login1',methods=['GET','POST'])
def login1():
	if request.method=='POST':
		str=do_the_login()
	else:
		str=show_the_login_form()
	return str