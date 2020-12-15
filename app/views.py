import re
from flask import render_template
from app import app,mongo
from bson.json_util import dumps

@app.route('/')
def home():
 #   query()
    return "hello"

@app.route('/test')
def test():
    return render_template('home.html')

@app.route('/search_id',methods=['GET','POST'])
def search_id():
    query = request.args.get('query')
    myquery = { "id": query }
    results = mongo.products.find(myquery)
    list_cur = list(results)
    json_data = dumps(list_cur)
    return json_data


@app.route('/search_content',methods=['GET','POST'])
def search_content():
    query = request.args.get('query')
    myquery = { 
            "$or":[
                    { "brand":  { "$regex": query }},
                    { "description": { "$regex": query }}
                ] 
            }
    results = mongo.products.find(myquery)
    list_cur = list(results)
    json_data = dumps(list_cur)
    return json_data
   
@app.route('/test_exact_brand',methods=['GET','POST'])
def test_exact_brand():
    query = "dsaasd"
    myquery = { "brand": query }
    results = mongo.products.find(myquery)
    list_cur = list(results)
    json_data = dumps(list_cur)
    return json_data

@app.route('/test_like_brand',methods=['GET','POST'])
def test_like_brand():
    query = "saa"
    myquery = { "brand": { "$regex": query } }
    results = mongo.products.find(myquery)
    list_cur = list(results)
    json_data = dumps(list_cur)
    return json_data



def isPalindrome(s):
    return s == s[::-1]

def halfPrice(s):
    return int(s/2)+(s/2 > 0)

