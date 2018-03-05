import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.serializers import NEW_BUSINESS_STRUCTURE, view_business_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('businesses', description='Operations related to Businesses')

@ns.route('/')
class RegisterBusiness(Resource):


    @ns.expect(NEW_BUSINESS_STRUCTURE, validate=True, code=201)
    #@api.doc(params={'id': 'An ID'})
    def post(self):
        """
        Register a business.
        """
        pass

    @ns.marshal_with(view_business_structure, envelope="data", code=201)
    def get(self):
        """
        Retrieves all businesses.
        """
        pass


@ns.route('/<int:businessId>')
@ns.response(404, 'Business not found')
class ShowBusiness(Resource):
    
    @ns.marshal_with(view_business_structure)
    def get(self, businessId):
        """
        Get a business.
        """
        pass

    @ns.response(204, 'Business deleted')
    def delete(self, businessId):
        """
        Remove a business.
        """
        pass


    @ns.expect(NEW_BUSINESS_STRUCTURE)
    @ns.marshal_with(NEW_BUSINESS_STRUCTURE)
    def put(self, businessId):
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