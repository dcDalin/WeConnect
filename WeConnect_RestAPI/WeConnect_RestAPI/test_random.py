import unittest
import json


from WeConnect_RestAPI.app import app as the_app, initialize_app

class TestSomething(unittest.TestCase):

    def setUp(self):
        # creates a test client
        test_app = initialize_app(the_app)
        self.app = test_app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass 

    
    def test_businesses_endpoint(self):
        # sends HTTP GET request to the businesses endpoint
        response = self.app.get('/api/v1/businesses/')
        self.assertEqual(response.status_code, 200) 


    def test_create_user(self):
        response = self.app.post('/api/v1/auth/register', data = {
            "firstName": '',
            "lastName": '',
            "email": '',
            "gender": '',
            "password": ''
        })
        self.assertEqual(response.status_code, 200)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()