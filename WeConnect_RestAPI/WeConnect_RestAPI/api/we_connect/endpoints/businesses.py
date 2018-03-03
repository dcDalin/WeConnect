import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.business import create_business
from WeConnect_RestAPI.api.we_connect.serializers import new_business_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('businesses', description='Operations related to Businesses')


@ns.route('/')
class RegisterBusiness(Resource):


    @api.expect(new_business_structure)
    def post(self):
        """
        Register a business.
        """
        pass

    @api.expect(new_business_structure)
    def get(self):
        """
        Retrieves all businesses.
        """
        pass


@ns.route('/<int:businessId>')
class ShowBusiness(Resource):
    

    def get(self):
        """
        Get a business.
        """
        pass

    def delete(self):
        """
        Remove a business.
        """
        pass

    def put(self):
        """
        Updates a business profile.
        """
        pass

    
@ns.route('/<int:businessId>/reviews')
class BusinessReviews(Resource):
    
    def post(self):
        """     
        Add a review for a business.
        """
        pass

    def get(self):
        """
        Get all reviews for a business.
        """
        pass