import datetime
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from WeConnect_RestAPI.api.restplus import api
from WeConnect_RestAPI.api.we_connect.custom_validation import is_empty, is_email, is_gender, is_password


class WeConnectUsers(object):

    def __init__(self):
        '''Constructor method, will have dictionaries in a list'''
        self.users_counter = 0
        self.users = []

        self.businesses = []

        self.reviews_counter = 0
        self.reviews = []

        self.the_token = ''

    def check_email_exists(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return True
        return False
    
    def check_business_email_exists(self, search_email):
        '''Check if business email exists'''
        for find_email in self.businesses:
            if find_email['business_email'] == search_email:
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
        # user['dateCreated'] = datetime.datetime.now()
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
            return {'message': 'User added'}
    

    
    def login_user(self, data):
        '''Logic behind logging in '''
        user = data
        if (is_empty(user['email'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}

        if is_email(user['email']):
            return {'message': 'Wrong email'}
            
        if not self.check_email_exists(user['email']):
            return {'message': 'Email does not exist'}
        
        a_variable = self.check_email_for_login(user['email'])

        if check_password_hash(a_variable['password'], user['password']):
            '''compare password input to saved password'''
            login_status = True
        if not login_status:
            return {'message': 'wrong creds'}
        global access_token
        global current_email
        current_email = user['email']
        access_token = create_access_token(identity=user['email'])
        self.the_token = access_token
        return {"access_token": access_token}

    def current_logged_in_user(self): 
        return access_token


    def show_all_users(self):
        return self.users


    '''Business related operations'''
    def create_business(self, data):
        business = data
        business['business_id'] = len(self.businesses) + 1
        business['user_email'] = current_email
        if (is_empty(business['business_name'])) or (is_empty(business['business_category'])) or (is_empty(business['business_email'])) or (is_empty(business['business_description'])) or (is_empty(business['business_phone'])):
            return {'message': 'Empty field(s)'}
        elif is_email(business['business_email']):
            return {'message': 'Wrong email'}
        elif self.check_business_email_exists(business['business_email']):
            return {'message': 'Email exists'}
        self.businesses.append(business)
        return {'message': 'Business added'}

    def show_all_businesses(self):
        return self.businesses

    def show_business_by_business_id(self, business_id):
        for business in self.businesses:
            if business['business_id'] == business_id:
                return business
        return {'message': 'Business not found'}

    def delete_business_by_business_id(self, business_id):
        business = self.show_business_by_business_id(business_id)
        if business['user_email'] != current_email:
            return {'message': 'You can only delete your business'}
        self.businesses.remove(business)
        return {'message': 'Business deleted'}

    def update_business_by_business_id(self, business_id, data):
        business = self.show_business_by_business_id(business_id)
        if business['user_email'] != current_email:
            return {'message': 'You can only update your business'}
        business.update(data)
        return {'message': 'Business updated'}
