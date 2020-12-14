import os
from flask import Flask
import pymongo

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'W-H]!/D/hHaRvY!+/z-|'
app.config.from_pyfile('config.py', silent=True)


client = pymongo.MongoClient("mongodb://productListUser:productListPassword@0.0.0.0:27017/")
mongo = client['promotions'] 

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from app import views
