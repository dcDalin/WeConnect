import unittest

from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers


class TestLogin(unittest.TestCase):

    def setUp(self):
        '''initialization'''
        self.init_we_connect_users = WeConnectUsers()

        self.data = {
            "email": "business@business.com",
            "password": "password"
        }

    def test_login_user(self):
        '''Test wrong email'''
        data = {
            "email": "businebusiness.com",
            "password": "password"
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Wrong email'})

    def test_empty_fields(self):
        '''Test empty fields'''
        data = {
            "email": "",
            "password": ""
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Empty field(s)'})
    
    def test_email_not_exist(self):
        '''Test empty fields'''
        data = {
            "email": "nonexistent@email.co",
            "password": "randompassword"
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Email does not exist'})

    # def test_wrong_password(self):
    #     '''Test if password is wrong'''
    #     data = {
    #         "first_name": "Dalin",
    #         "last_name": "Oluoch",
    #         "gender": "Male",
    #         "email": "nonexistent@email.co",
    #         "password": "Pas834**2Ss#"
    #     }
    #     data2 = {
    #         "email": "nonexistent@email.co",
    #         "password": "Pas834**sss#"
    #     }
    #     self.init_we_connect_users.create_user(data)
    #     response = self.init_we_connect_users.login_user(data2)
    #     self.assertEqual(response,{'message': 'wrong creds'})

if __name__ == '__main__':
    unittest.main()