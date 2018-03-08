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

    def test_check_email_for_login(self):
        mail = 'random@mail.com'
        response = self.init_we_connect_users.check_email_for_login(mail)
        self.assertFalse(response)
    def test_check_email_for_login_true(self):
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA111"
        }
        mail = 'mcdalinoluoch@gmail.com'
        self.init_we_connect_users.create_user(data)
        response = self.init_we_connect_users.check_email_for_login(mail)
        self.assertEqual(response, data)

    def test_login_empty_fields(self):
        data = {
            "email": "",
            "password": ""
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Empty field(s)'})

    def test_login_password_length(self):
        data = {
            "email": "rea@email.com",
            "password": "aaAAe1"
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Password is less than 8 characters'})

    def test_login_wrong_email(self):
        data = {
            "email": "reail.com",
            "password": "aaAAe1332a"
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Wrong email'})

    def test_login_email_not_exist(self):
        data = {
            "email": "rea@il.com",
            "password": "aaAAe1332a"
        }
        response = self.init_we_connect_users.login_user(data)
        self.assertEqual(response, {'message': 'Email does not exist'})

if __name__ == '__main__':
    unittest.main()