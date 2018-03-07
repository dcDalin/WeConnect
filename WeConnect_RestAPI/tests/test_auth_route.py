import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import unittest
import json
from WeConnect_RestAPI.app import app as the_app, initialize_app


class TestAuthRoute(unittest.TestCase):

    def setUp(self):
        # creates a test client
        test_app = initialize_app(the_app)
        self.app = test_app.test_client()
        self.app.testing = True
        self.bucketlist = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "email": "mcdalin@gmaol.co",
            "gender": "male",
            "password": "password"
        }

    def tearDown(self):
        pass


    def test_all_users_endpoint(self):
        #test if new user is successfuly created
        response = self.app.get('/api/v1/auth/all-users')
        self.assertEqual(response.status_code, 401)

    def test_bucketlist_creation(self):
        """Test API can create a bucketlist (POST request)"""
        pass


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
