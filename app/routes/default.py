from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/') #ask why this isnt working
def index():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

#making your own route
@app.route('/overview')
def overview():
    return render_template('overview.html')