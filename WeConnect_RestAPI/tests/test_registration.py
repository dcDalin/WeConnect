import unittest

from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers


class TestRegistration(unittest.TestCase):

    def setUp(self):
        '''initialization'''
        self.init_test_registration = WeConnectUsers()

        self.data = {
            "first_name": "Example",
            "last_name": "Example",
            "gender": "Female",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA111"
        }

    def test_check_email_exists_false(self):
        '''Check if email does not exist'''
        response = self.init_test_registration.check_email_exists('email@email.com')
        self.assertFalse(response)

    def test_check_email_exists_true(self):
        '''Check if email exist'''
        self.init_test_registration.create_user(self.data)
        response = self.init_test_registration.check_email_exists('mcdalinoluoch@gmail.com')
        self.assertTrue(response)
    

    def test_empty_fields(self):
        '''Test if input is null'''
        data = {
            "first_name": "",
            "last_name": "",
            "gender": "",
            "email": "",
            "password": ""
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'Empty field(s)'})
        
    def test_name_length(self):
        '''Test if input length'''
        data = {
            "first_name": "s",
            "last_name": "s",
            "gender": "Male",
            "email": "email@email.com",
            "password": "aaaAAA111"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'Name too short'})

    def test_valid_email(self):
        '''Test if email is valid'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "email@emai",
            "password": "aaaAAA111"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'Wrong email'})

    

    def test_email_exists(self):
        '''Test if email already exists'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA111"
        }
        data2 = {
            "first_name": "Someone",  
            "last_name": "Else",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA111"
        }
        self.init_test_registration.create_user(data)
        response = self.init_test_registration.create_user(data2)
        self.assertEqual(response, {'message': 'Email exists'})

    def test_gender_input(self):
        '''Test if gender input is valid'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Massle",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA111"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'Wrong gender'})

    def test_password_length_input(self):
        '''Test if password length input is valid'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAA1"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'Password is less than 8 characters'})

    def test_no_numbers_password(self):
        '''Test if password has no numbers'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaaAAAaaaa"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'No numbers present'})

    def test_no_capital_letters(self):
        '''Test if password has no capital letters'''
        data = {
            "first_name": "Dalin",
            "last_name": "Oluoch",
            "gender": "Male",
            "email": "mcdalinoluoch@gmail.com",
            "password": "aaa123aaa3"
        }
        response = self.init_test_registration.create_user(data)
        self.assertEqual(response, {'message': 'No capital letters present'})
        

    def test_registration(self):
        '''Test if new_user_is_added'''
        response = self.init_test_registration.create_user(self.data)
        self.assertEqual(response, {'message': 'User added'})    

if __name__ == '__main__':
    unittest.main()
