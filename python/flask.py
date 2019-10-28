# RUN FLASK
# export FLASK_APP=app.py (indicate path to flask where app is)
# flask run (flask server is set up)
# http://127.0.0.1:5000/

# flask can be used in the free python server pythonanywhere.com
# it has 500mb of disk space
# note, to check their package versions so there is no conflicts with your local packages interms of codes & models


# Pass variables from Flask to HTML ----------------------
# in flask, use render template
from flask import Flask, render_template

@app.route('/')
def index(name=None):
    login = 'test success'
    return render_template('index.html',name=name, login=login)

# in html
{{variable name}}