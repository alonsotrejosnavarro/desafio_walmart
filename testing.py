import unittest
from app import app
from app.utils import isPalindrome,halfPrice

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
        self.assertEqual(isPalindrome('asddsa'),True)

    def test_isPalindromeFalse(self):
        self.assertEqual(isPalindrome('asdf'),False)      

    def test_halfPrice(self):
        self.assertEqual(halfPrice(8),4)

    def test_halfPrice(self):
        self.assertEqual(halfPrice(5),3)


if __name__ == "__main__":
    unittest.main()


