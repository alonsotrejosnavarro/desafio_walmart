import re
from flask import render_template,request
from app import app,mongo
from bson.json_util import dumps

@app.route('/')
def home():
    return "hello"

@app.route('/test')
def test():
    return render_template('home.html')

@app.route('/search_content',methods=['GET','POST'])
def search_content():

    query = request.args.get('query')
    
    #Si query es numerica puede ser busqueda de id
    #Si no es numerica se aplica validacion de largo 3

    if  (not query.isnumeric()) and len(query) < 3:
        return "error largo_query"

    if(query.isnumeric()):
        myquery = { "id": int(query)  }
    else:    
        myquery = { 
          "$or":[
                 { "brand":  { "$regex": query }},
                 { "description": { "$regex": query }}
               ] 
        }
    results = mongo.products.find(myquery)
    list_cur = list(results)

    #Si es palindrome, aplicamos mitad de precio
    if isPalindrome(query):
        temp_list = list()

        for el in list_cur:
            el['price'] = halfPrice(el['price'])
            temp_list.append(el)
        list_cur = temp_list

    json_data = dumps(list_cur)
    return json_data

def isPalindrome(s):
    return s == s[::-1]

def halfPrice(s):
    return int(s/2)+(s/2 > 0)

