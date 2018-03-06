import unittest
import json
from WeConnect_RestAPI.app import app as the_app, initialize_app


class TestAuthRoute(unittest.TestCase):

    def setUp(self):
        # creates a test client
        test_app = initialize_app(the_app)
        self.app = test_app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass 


    def test_create_user(self):
        #test if new user is successfuly created
        response = self.app.post('/api/v1/auth/register', data = {
            "firstName": 'Test',
            "lastName": 'Test',
            "email": 'test@test.com',
            "gender": 'Female',
            "password": 'password'
        })
        self.assertEqual(response.status_code, 200)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()