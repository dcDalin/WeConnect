import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.business import WeConnect
from WeConnect_RestAPI.api.we_connect.serializers import NEW_BUSINESS_STRUCTURE, view_business_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('businesses', description='Operations related to Businesses')

initWeConnect = WeConnect()

@ns.route('/')
class RegisterBusiness(Resource, WeConnect):


    @ns.expect(NEW_BUSINESS_STRUCTURE, validate=True, code=201)
    #@api.doc(params={'id': 'An ID'})
    def post(self):
        """
        Register a business.
        """
        return initWeConnect.create_business(api.payload)

    @ns.marshal_with(view_business_structure, envelope="data", code=201)
    def get(self):
        """
        Retrieves all businesses.
        """
        return initWeConnect.show_all_businesses()


@ns.route('/<int:businessId>')
@ns.response(404, 'Business not found')
class ShowBusiness(Resource):
    
    @ns.marshal_with(view_business_structure)
    def get(self, businessId):
        """
        Get a business.
        """
        return initWeConnect.show_business_by_businessId(businessId)

    @ns.response(204, 'Business deleted')
    def delete(self, businessId):
        """
        Remove a business.
        """
        initWeConnect.delete_business_by_businessId(businessId)
        return '', 204


    @ns.expect(NEW_BUSINESS_STRUCTURE)
    @ns.marshal_with(NEW_BUSINESS_STRUCTURE)
    def put(self, businessId):
        """
        Updates a business profile.
        """
        return initWeConnect.update_business_by_businessId(businessId, api.payload)

    
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