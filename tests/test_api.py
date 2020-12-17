import unittest
from flask import Flask
from flask_testing import TestCase
from requests import get, head

PREFIX = 'http://127.0.0.1:5000/'

class TestApiResponse(TestCase):
    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_200(self):
        URL = PREFIX + 'api/password/random'
        r = head(URL) # e.g. <Response [200]>
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password/random?limit=2'
        r = head(URL)
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password?words=cat&words=computer'
        r = head(URL)
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password?words=cat&words=computer?limit=2'
        r = head(URL)
        self.assertEqual(r.status_code , 200)
    



"""

response = get(URL1)
print(response.json())
response = get(URL2)
print(response.json())
"""

if __name__ == '__main__':
    unittest.main()