STEP 0:
The application will be installed and run as python package.
the static folder  is the place where CSS and JavaScript files go.
Inside the templates folder, Flask will look for Jinja2 templates.

STEP 1:
Database Schema

STEP 2:
Application Setup Code
1. flaskr/flaskr/flaskr.py
2. For small applications like flaskr, it is possible to drop the configuration directly into the module. However, a cleaner solution is to create a separate .ini or .py file, load that, and import the values from there.
3. Now that the schema is in place, you can create the application module, flaskr.py.

Step 4: 
Database Connections
1. Flask provides two contexts:application context and request context.
2. the request variable is the request object associated with the current request
3. g is a general purpose variable associated with the current application context.
4. For the time being, all you have to know is that you can store information safely on the g object.
 

