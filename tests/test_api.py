import unittest
import passwordgenerator
from requests import get, head

PREFIX = 'http://127.0.0.1:5000'

class TestApiResponse(unittest.TestCase):
    def test_200(self):
        URL = PREFIX + '/api/password/random'
        r = head(URL) 
        self.assertEqual(r.status_code , 200)

        URL = PREFIX + '/api/password/random'
        r = head(URL) # e.g. <Response [200]>
        self.assertEqual(r.status_code , 200)
    



"""

response = get(URL1)
print(response.json())
response = get(URL2)
print(response.json())
"""

if __name__ == '__main__':
    unittest.main()