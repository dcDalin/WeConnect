import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.business import WeConnect
from WeConnect_RestAPI.api.we_connect.serializers import new_business_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('businesses', description='Operations related to Businesses')

initWeConnect = WeConnect()

@ns.route('/')
class RegisterBusiness(Resource, WeConnect):



    @api.expect(new_business_structure)
    @ns.marshal_with(new_business_structure, code=201)
    def post(self):
        """
        Register a business.
        """
        pass

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