import datetime
from WeConnect_RestAPI.api.restplus import api

class WeConnectUsers(object):
    

    def __init__(self):
        '''Constructor method, will have dictionaries in a list'''
        self.users_counter = 0
        self.users = []
  
    def create_user(self, data):
        user = data
   
        self.users.append(user) 
        return {'result': 'User added'}, 201

    def show_all_users(self):
        return self.users
