import unittest
from flask import Flask
from flask_testing import TestCase
from passwordgenerator import app, API_RESPONSE_LIMIT

PREFIX = 'http://127.0.0.1:5000/'

class TestApiResponse(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_200(self):
        URL = PREFIX + 'api/password/random'
        r = self.client.head(URL) # e.g. <Response [200]>
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password/random?limit=2'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password?words=cat&words=computer'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + 'api/password?words=cat&words=computer&limit=2'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 200)

        """ 
        TODO: fix this
        returns a type error only when run from __main__
        """
        URL = PREFIX + 'api/password'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 200)       
    
    def test_422(self):
        URL = PREFIX + 'api/password/random?limit=' + str(API_RESPONSE_LIMIT + 1)
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 422)

        URL = PREFIX + 'api/password?words=cat&words=computer&limit=' + str(API_RESPONSE_LIMIT + 1)
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 422)
    
    def test_404(self):
        URL = PREFIX + 'api'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 404)   

        URL = PREFIX + 'api'
        r = self.client.head(URL)
        self.assertEqual(r.status_code , 404)        

if __name__ == '__main__':
    unittest.main()