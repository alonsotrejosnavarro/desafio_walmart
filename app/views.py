import re
from flask import render_template,request,redirect,url_for,jsonify
from app import app,mongo
from app.forms import searchForm
from bson.json_util import dumps

@app.route('/')
def home():
    form = searchForm()
    #if form.validate_on_submit():
    #    return redirect_url(url_for('/'))
    return render_template('home.html',title = 'Home',form=form)

@app.route('/search_content',methods=['GET','POST'])
def search_content():

    query = request.args.get('query')
    #Si query es numerica puede ser busqueda de id
    #Si no es numerica se aplica validacion de largo 3

    if  (not query.isnumeric()) and len(query) < 3:
        return jsonify(productos = "error largo_query")

    if(query.isnumeric()):
        myquery = { "id": int(query)  }
    else:    
        myquery = { 
          "$or":[
                 { "brand":  { "$regex": query }},
                 { "description": { "$regex": query }}
               ]
        }

    results = mongo.products.find(myquery,{ "_id": False })
    list_cur = list(results)


    #Si es palindrome, aplicamos mitad de precio
    if isPalindrome(query):
        temp_list = list()

        for el in list_cur:
            el['price'] = halfPrice(el['price'])
            

            temp_list.append(el)
        list_cur = temp_list
 
    return jsonify(productos = list_cur)

def isPalindrome(s):
    return s == s[::-1]

def halfPrice(s):
    return int(s/2)+(s/2 > 0)

