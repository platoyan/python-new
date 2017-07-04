#Static Files
#Just create a folder called static in your package or next to your module and it will be available at /static on the application.
#url_for('static', filename='style.css') #static/style.css

#Rendering Templates
# Flask configures the Jinja2 template engine 
from flask import render_template,Flask
app=Flask(__name__)
@app.route('/he/')
@app.route('/he/<name>')
def he(name=None):
	return render_template('he.html',name=name)

