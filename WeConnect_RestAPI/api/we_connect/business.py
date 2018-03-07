import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from WeConnect_RestAPI.api.restplus import api
from WeConnect_RestAPI.api.we_connect.custom_validation import is_empty, is_email, is_gender, is_password

class WeConnectUsers(object):
    

    def __init__(self):
        '''Constructor method, will have dictionaries in a list'''
        self.users_counter = 0
        self.users = []
        self.token = []
  
    def check_email_exists(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return True
        return False 

    def check_email_for_login(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return find_email
        return False 

    def check_password_exists(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return True
        return False 


    def create_user(self, data):
        user = data
        user['user_id'] = self.users_counter = self.users_counter + 1
        user['password'] = generate_password_hash(user['password'])
        #user['dateCreated'] = datetime.datetime.now()
        if (is_empty(user['first_name'])) or (is_empty(user['last_name'])) or (is_empty(user['email'])) or (is_empty(user['gender'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}
        elif is_email(user['email']):
            return {'message': 'Wrong email'}
        elif self.check_email_exists(user['email']):
            return {'message': 'Email exists'}
        elif is_gender(user['gender']):
            return {'message': 'Wrong gender'}
        elif is_password(user['password']):
            return {'message': 'Weak password'}
        else:
            user['first_name'] = user['first_name'].title()
            user['last_name'] = user['last_name'].title()
            self.users.append(user)
            return {'message': 'successful'}
 
    def show_all_users(self):
        return self.users

    def login_user(self, data):
        '''Logic behind logging in '''
        user = data
        if (is_empty(user['email'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}
        elif is_email(user['email']):
            return {'message': 'Wrong email'}
        elif not self.check_email_exists(user['email']):
            return {'message': 'Email does not exist'}
        else:
            a_variable = self.check_email_for_login(user['email'])
            if check_password_hash(a_variable['password'], user['password']):
                '''compare password input to saved password'''
                return {'message': 'logged in'}
            return {'message': 'wrong creds'}