from flask import render_template
from app import app
#from mongo_query import query

@app.route('/')
def home():
 #   query()
    return "<b>There has been a change</b>"


@app.route('/template')
def template():
    return render_template('home.html')
