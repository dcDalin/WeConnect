import unittest


from WeConnect_RestAPI.api.we_connect.business import WeConnect


class TestWeConnect(unittest.TestCase):
    
    
    def setUp(self):
        '''initialization'''
        self.initWeConnect = WeConnect()

    def test_create_business(self):
        pass

    def test_view_businesses(self):
        pass

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