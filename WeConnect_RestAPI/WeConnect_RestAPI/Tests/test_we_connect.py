import unittest


from WeConnect_RestAPI.api.we_connect.business import WeConnect


class TestWeConnect(unittest.TestCase):
    """This class represents the WeConnect test case"""

    def setUp(self):
        '''initialization'''
        self.initWeConnect = WeConnect()
        self.data = {
            "businessCategory": "Services",
            "businessEmail": "info@pink.com",
            "businessName": "Pink Seat",
            "date_created": "2018-03-03T19:58:42.316000+00:00"
        }

    def test_create_business(self):
        '''Test if a new business is created'''
        response = self.initWeConnect.create_business(self.data)
        self.assertEqual(response, self.data, msg="Input is not what is being returned by create_business()")

    def test_view_all_businesses(self):
        '''Test if a new business created is in the list of businesses'''
        add_business = self.initWeConnect.create_business(self.data)
        all_businesses = self.initWeConnect.show_all_businesses()
        self.assertIn(add_business, all_businesses, msg="Input is not what is being returned by create_business()")

    def test_view_business_by_id(self):
        pass

    def test_edit_business(self):
        pass

    def test_delete_business(self):
        pass


    def test_create_user(self):
        pass

    def test_view_users(self):
        pass

    def test_view_user_by_id(self):
        pass

    def test_edit_user(self):
        pass

    def test_delete_user(self):
        pass



if __name__ == '__main__':
    unittest.main()
