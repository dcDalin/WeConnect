import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from WeConnect_RestAPI.api.restplus import api
from WeConnect_RestAPI.api.we_connect.custom_validation import is_empty, is_email

class WeConnectUsers(object):
    

    def __init__(self):
        '''Constructor method, will have dictionaries in a list'''
        self.users_counter = 0
        self.users = []
  
    def create_user(self, data):
        user = data
        user['userId'] = self.users_counter = self.users_counter + 1
        user['password'] = generate_password_hash(user['password'])
        #user['dateCreated'] = datetime.datetime.now()
        if (is_empty(user['firstName'])) or (is_empty(user['lastName'])) or (is_empty(user['email'])) or (is_empty(user['gender'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}
        elif is_email(user['email']):
            return {'message': 'Wrong email'}
        else:
            self.users.append(user)
            return user



    def show_all_users(self):
        return self.users
