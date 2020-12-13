import pymongo
from pprint import pprint   

client = pymongo.MongoClient("mongodb://productListUser:productListPassword@127.0.0.1:27017/")

db = client['promotions'];
col = db.products

def query():
    myquery = { "brand": "dsaasd" }
    mydoc = col.find(myquery)
    for x in mydoc:
        print(x)

query()
