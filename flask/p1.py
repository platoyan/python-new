from flask import Flask
app = Flask(__name__) #An instance of Flask will be an WSGI application
                      #First argument is the name of the application's module or package.
                      #if you are using a single module,you should use __name__
                      #This is needed so that Flask knows where to look for templates, static files, and so on
                      #

@app.route('/')
def hw():
	return 'hw'

# run the application:
# for linux: $ export FLASK_APP=p1.py
# 			 $ flask run
# 			 or
# 			 $ export FLASK_APP=p1.py
# 			 $ python -m flask run
# for windows:use set instead of export
# you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:
# 			 flask run --host=0.0.0.0
# 			 This tells your operating system to listen on all public IPs.
# If you enable debug support the server will reload itself on code changes
# 			 $ export FLASK_DEBUG=1