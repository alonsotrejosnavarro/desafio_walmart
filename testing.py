import unittest
import pymongo
import dns
import requests
import json
from app import app
from app import views

client = pymongo.MongoClient("mongodb+srv://productListUser:productListPassword@cluster0.glk1i.mongodb.net/?retryWrites=true&w=majority",
        tls=True,
        tlsAllowInvalidCertificates=True)

mongo = client['promotions']

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['Testing'] = True
        app.config['Debug'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_root(self):
        response = self.app.get('/',follow_redirects = True)
        self.assertEqual(response.status_code,200)

    def test_isPalindromeTrue(self):
        self.assertEqual(views.isPalindrome('asddsa'),True)

    def test_isPalindromeFalse(self):
        self.assertEqual(views.isPalindrome('asdf'),False)      

    def test_halfPrice(self):
        self.assertEqual(views.halfPrice(8),4)

    def test_halfPrice(self):
        self.assertEqual(views.halfPrice(5),3)

    def test_queryExistingId(self):
        response = self.app.get('/search_content',query_string=dict(query='18') ,follow_redirects = True)
        j = json.loads(response.data)
        self.assertEqual(j[0]['id'],18) 

    def test_tooSmallQuery(self):
        response = self.app.get('/search_content',query_string=dict(query='ds') ,follow_redirects = True)
        self.assertEqual(response.data,"error largo_query")

    def test_exactBrand(self):
        response = self.app.get('/search_content',query_string=dict(query='dsaasd') ,follow_redirects = True)
        self.assertNotEqual(response.data,[]) 

    def test_brandContains(self):
        response = self.app.get('/search_content',query_string=dict(query='saa') ,follow_redirects = True)
        self.assertNotEqual(response.data,[]) 
    
    def test_descriptionContains(self):
        response = self.app.get('/search_content',query_string=dict(query='bvp') ,follow_redirects = True)
        self.assertNotEqual(response.data,[]) 

    def test_queryNonExistingId(self):
        response = self.app.get('/search_content',query_string=dict(query='3001') ,follow_redirects = True)
        j = json.loads(response.data)
        self.assertEqual(j,[]) 

    def test_queryNonExistingBrandOrDescription(self):
        response = self.app.get('/search_content',query_string=dict(query='un elefante se balanceaba') ,follow_redirects = True)
        j = json.loads(response.data)
        self.assertEqual(j,[]) 

    def test_queryHalfPrice(self):
        response = self.app.get('/search_content',query_string=dict(query='dsaasd') ,follow_redirects = True)
        j = json.loads(response.data)
        self.assertEqual(j[0]['price'],65087) 


if __name__ == "__main__":
    unittest.main()


