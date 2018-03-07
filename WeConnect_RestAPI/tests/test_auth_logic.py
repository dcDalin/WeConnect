import unittest

from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers


class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        '''initialization'''
        self.init_we_connect_users = WeConnectUsers()

    def test_registration(self):
        '''Test if new_user_is_added'''
        response = self.init_we_connect_users.create_user('Dalin', 712876245)
        self.assertEqual(response, 'contact added')
    
    def test_phone_number_exists(self):
        '''     
            Create new contact and see if number entries
        '''
        self.initPhoneBook.add_contact('Nancy', 712872452)

        response = self.initPhoneBook.phone_number_exists(712872452)
        self.assertTrue(response)

    def test_show_all_contacts(self):
        '''
            Test to see if all contacts are shown
            Create some contacts before we search for them
        '''
        self.initPhoneBook.add_contact('Nancy', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)

        response = self.initPhoneBook.show_all_contacts()
        self.assertEqual(response, [{'phone': 712872452, 'id': 1, 'name': 'Nancy'}, {'phone': 712876245, 'id': 2, 'name': 'Mwangi'}])

    def test_check_phone_number_is_int(self):
        '''Test if phone number is integer'''
        response = self.initPhoneBook.add_contact('Dalin', 'adfi')
        self.assertEqual(response, 'not a number')

    def test_phone_number_length_is_not_nine(self):
        response = self.initPhoneBook.add_contact('Dalin', 3456789)
        self.assertEqual(response, 'number short or long')

    def test_search_contact_name(self):
        '''Create some contacts before we search for them'''
        self.initPhoneBook.add_contact('Mike', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)

        response = self.initPhoneBook.search_contact_name('Mwangi')
        self.assertTrue(response)

    def test_search_contact_phone(self):
        '''Create some contacts before we search for them'''
        self.initPhoneBook.add_contact('Mike', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)

        response = self.initPhoneBook.search_contact_phone(712876245)
        self.assertEqual(response, [{'id': 2, 'name': 'Mwangi', 'phone': 712876245}])

    def test_contact_does_not_exist(self):
        '''Create some contacts before we search for them'''
        self.initPhoneBook.add_contact('Mike', 712872452)
        self.initPhoneBook.add_contact('Mwangi', 712876245)
 
        response = self.initPhoneBook.search_contact_name('Nancy')
        self.assertFalse(response)

    def test_edit_phone_number(self):
        '''
            Create a contact before we can edit it
            Edit function takes in the name of the person and the new phone number
        '''
        self.initPhoneBook.add_contact('Ann', 712876245)

        response = self.initPhoneBook.edit_phone_number('Ann', 765356999)
        self.assertEqual(response, [{'id': 1, 'name': 'Ann', 'phone': 765356999}])

    def test_delete_contact(self):
        '''
            Create a contact that we will delete
        '''
        self.initPhoneBook.add_contact('Ann', 712676245)

        response = self.initPhoneBook.delete_contact('Ann')
        self.assertEqual(response, 'contact deleted')        

if __name__ == '__main__':
    unittest.main()