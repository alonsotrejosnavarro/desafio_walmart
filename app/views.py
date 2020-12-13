from flask import render_template
from app import app
import mongo_query 
from utils import isPalindrome,halfPrice

@app.route('/','/home')
def home():
 #   query()
    return "<b>There has been a change1</b>"


@app.route('/test')
def template():
    return render_template('home.html')

@app.route('/search_id')
def template():
    myquery = { "id": "/"+query+"/" }
    results = mongo.db.products.find(myquery)
    return results


@app.route('/search_brand')
def template():
    myquery = { "brand": "/"+query+"/" }
    results = mongo.db.products.find(myquery)
    return results

@app.route('/search_description')
def template():
    myquery = { "description": "/"+query+"/" }
    results = mongo.db.products.find(myquery)
    return results


