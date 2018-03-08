import unittest

from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers


class TestAuthLogic(unittest.TestCase):

    def setUp(self):
        '''initialization'''
        self.init_we_connect_users = WeConnectUsers()

        self.data = {
            "business_name": "Example",
            "business_category": "Service",
            "business_email": "business@business.com",
            "business_description": "the example business",
            "business_phone": "0827372733"
        }

    # def test_new_business(self):
    #     '''Test if new_user_is_added'''
    #     response = self.init_we_connect_users.create_business(self.data)
    #     self.assertEqual(response, {'message': 'Business added'})

if __name__ == '__main__':
    unittest.main()
 