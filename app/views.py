from flask import render_template
from app import app,mongo
from bson.json_util import dumps
import utils

@app.route('/')
def home():
 #   query()
    return "hello"

@app.route('/test')
def test():
    return render_template('home.html')

#@app.route('/search_id',methods=['GET','POST'])
#def search_id():
#    query = request.args.get('query')
#    myquery = { "id": "/"+query+"/" }
#    results = mongo.products.find(myquery)
#    return results


#@app.route('/search_brand',methods=['GET','POST'])
#def search_brand():
#    query = request.args.get('query')
#    myquery = { "brand": "/"+query+"/" }
#    results = mongo.products.find(myquery)
#    return results

#@app.route('/search_description',methods=['GET','POST'])
#def search_description():
#    query = request.args.get('query')
#    myquery = { "description": "/"+query+"/" }
#    results = mongo.products.find(myquery)
#    return results

@app.route('/test_brand',methods=['GET','POST'])
def test_brand():
    query = "dsaasd"
    myquery = { "brand": query }
    results = mongo.products.find(myquery)
    list_cur = list(results)
    json_data = dumps(list_cur)
    print(json_data)
    return json_data
