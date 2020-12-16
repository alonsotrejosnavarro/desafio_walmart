import os
import dns
from flask import Flask
from flask_bootstrap import Bootstrap
import pymongo

app = Flask(__name__)
app.config['TESTING'] = True
app.config['SECRET_KEY'] = 'W-H]!/D/hHaRvY!+/z-|'
app.config.from_pyfile('config.py', silent=True)
bootstrap = Bootstrap(app)
    
#client = pymongo.MongoClient("mongodb://productListUser:productListPassword@0.0.0.0:27017/")
client = pymongo.MongoClient("mongodb+srv://productListUser:productListPassword@cluster0.glk1i.mongodb.net/?retryWrites=true&w=majority",
        tls=True,
        tlsAllowInvalidCertificates=True)

mongo = client['promotions'] 

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from app import views
