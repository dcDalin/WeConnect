
#! /WeConnect_RestAPI/api/we_connect business
# -*- coding: utf-8 -*-
"""Core logic to the auth and businesses namespaces

Contains WeConnectUsers class which has various methods interacting with the API
"""

import re
import datetime

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

from WeConnect_RestAPI.api.restplus import api
from WeConnect_RestAPI.api.we_connect.custom_validation import is_empty, is_email, is_gender


class WeConnectUsers(object):

    def __init__(self):
        '''Constructor method, will have dictionaries in a list

        This will act as some sort of database
        '''
        self.users_counter = 0
        self.users = []
        self.businesses = []
        self.reviews = []
        self.the_token = ''

    #Registration related methods
    def check_email_exists(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return True
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
        if (is_empty(user['first_name'])) or (is_empty(user['last_name'])) or (is_empty(user['email'])) or (is_empty(user['gender'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}
        if len(user['first_name']) < 3 or len(user['last_name']) < 3:
            return {'message': 'Name too short'}
        if is_email(user['email']):
            return {'message': 'Wrong email'}
        if self.check_email_exists(user['email']):
            return {'message': 'Email exists'}
        if is_gender(user['gender']):
            return {'message': 'Wrong gender'}
        if len(user['password']) < 8:
            return {'message': 'Password is less than 8 characters'}
        if re.search('[0-9]', user['password']) is None:
            return {'message': 'No numbers present'}
        if re.search('[A-Z]', user['password']) is None: 
            return {'message': 'No capital letters present'}
        
        user['password'] = generate_password_hash(user['password'])
        user['first_name'] = user['first_name'].title()
        user['last_name'] = user['last_name'].title()
        self.users.append(user)
        return {'message': 'User added'}
    

    #Login related operations
    def check_email_for_login(self, search_email):
        '''Check if email'''
        for find_email in self.users:
            if find_email['email'] == search_email:
                return find_email
        return False

    def login_user(self, data):
        '''Logic behind logging in '''
        user = data
        if (is_empty(user['email'])) or (is_empty(user['password'])):
            return {'message': 'Empty field(s)'}
        
        if len(user['password']) < 8:
            return {'message': 'Password is less than 8 characters'}

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
        return {"access_token": access_token, "message": "Logged in"}

    def current_logged_in_user(self): 
        return access_token

    #Reset password related operations
    def reset_password(self, data):
        for user in self.users:
            if user['email'] == current_email:        
                user.update(data)
        return {'message': 'Password updated'}

    #Business related operations
    def check_business_email_exists(self, search_email):
        '''Check if business email exists'''
        for find_email in self.businesses:
            if find_email['business_email'] == search_email:
                return True
        return False

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
        for business in self.businesses:
            if business['business_id'] == business_id:
                if business['user_email'] != current_email:
                    return {'message': 'You can only delete your business'}
                self.businesses.remove(business)
                return {'message': 'Business deleted'}
        return {'message': 'Business not found'}

    def update_business_by_business_id(self, business_id, data):
        for business in self.businesses:
            if business['business_id'] == business_id:
                if business['user_email'] != current_email:
                    return {'message': 'You can only update your business'}
                business.update(data)
                return {'message': 'Business updated'}
        return {'message': 'Business not found'}

    
    #Business reviews related operations
    def add_review_to_businesss(self, business_id, data):
        for business in self.businesses:
            if business['business_id'] == business_id:        
                review = data
                review['review_id'] = len(self.reviews) + 1
                review['business_id'] = business_id
                review['user_email'] = current_email 
                review['date_created'] = datetime.datetime.now()     
                self.reviews.append(review)
                return {'message': 'Review added'}
        return {'message': 'Business with the ID not found'}


    def view_business_reviews(self, business_id):
        for business in self.businesses:
            if business['business_id'] == business_id:
                for review in self.reviews:
                    if review['business_id'] == business_id:
                        return review
                return {'message': 'Review for business not found'}
        return {'message': 'Business with the ID not found'}