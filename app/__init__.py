import os
from flask import Flask
from Flask-Pymongo import PyMongo

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'W-H]!/D/hHaRvY!+/z-|'
app.config['MONGO_URI'] = 'mongodb://productListUser:productListPassword@127.0.0.1:27017/promotions'
app.config.from_pyfile('config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from app import views
