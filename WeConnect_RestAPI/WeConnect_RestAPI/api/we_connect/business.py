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
  
    def create_user(self): 
        pass

    def create_business(self, data):
        business = data
        business['businessId'] = self.business_counter = self.business_counter + 1
        business['date_created'] = datetime.datetime.now()
        if (business['businessCategory'].strip() == '') or (business['businessEmail'].strip() == '') or (business['businessName'].strip() == ''):
            return {'error': 'Empty field(s)'}
        else:
            self.businesses.append(business)
            return {'result': 'Business added'}, 201

    def show_all_businesses(self):
        return self.businesses

    def show_business_by_businessId(self, businessId):
        for business in self.businesses:
            if business['businessId'] == businessId:
                return business
            api.abort(404, "Todo {} doesn't exist".format(businessId))

    def update_business_by_businessId(self, businessId, data):
        business = self.show_business_by_businessId(businessId)
        business.update(data)
        return business


    def delete_business_by_businessId(self, businessId):
        business = self.show_business_by_businessId(businessId)
        self.businesses.remove(business)

    