import datetime
from WeConnect_RestAPI.api.restplus import api

class WeConnect(object):
    

    def __init__(self):
        '''Constructor method, will have dictionaries in a list'''
        self.users_counter = 0
        self.users = []

        self.business_counter = 0
        self.businesses = []

        self.reviews_counter = 0
        self.reviews = []