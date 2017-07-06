#Accessing Request Data
#In Flask this information is provided by the global request object
#Certain objects in Flask are global objects, but not of usual kind.There objects are actually proxies to objects that are local to specific context.
from flask import request,Flask
app=Flask(__name__)
#The easiest solution for unit testing is to use the test_request_context()
with app.test_request_context('/hello',method='POST'):
	assert request.path=='/hello'
	assert request.method=='POST'
#The other possibility is passing a whole WSGI environment to the request_context() method:
with app.request_context(environ):
	assert request.method == 'POST'
