import unittest

from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers


class TestAuthLogic(unittest.TestCase):

    def setUp(self):
        '''initialization'''
        self.init_we_connect_users = WeConnectUsers()

        self.data = {
            "first_name": "Example",
            "last_name": "Example",
            "gender": "Female",
            "email": "mcd@sd.co",
            "password": "password"
        }

    def test_empty_fields(self):
        '''Test if input is null'''
        data = {
            "first_name": "",
            "last_name": "",
            "gender": "",
            "email": "",
            "password": ""
        }
        response = self.init_we_connect_users.create_user(data)
        self.assertEqual(response, {'message': 'Empty field(s)'})

    def test_valid_email(self):
        '''Test if email is valid'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "somsd",
            "password": "password"
        }
        response = self.init_we_connect_users.create_user(data)
        self.assertEqual(response, {'message': 'Wrong email'})

    def test_registration(self):
        '''Test if new_user_is_added'''
        response = self.init_we_connect_users.create_user(self.data)
        self.assertEqual(response, {'message': 'successful'})

    def test_email_exists(self):
        '''Test if email already exists'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "password"
        }
        data2 = {
            "first_name": "Someone",
            "last_name": "Else",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "password"
        }
        self.init_we_connect_users.create_user(data)
        response = self.init_we_connect_users.create_user(data2)
        self.assertEqual(response, {'message': 'Email exists'})

        
if __name__ == '__main__':
    unittest.main()