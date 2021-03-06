import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.restplus import api
from WeConnect_RestAPI.api.we_connect.authentication import token_required
from WeConnect_RestAPI.api.we_connect.serializers import NEW_BUSINESS_STRUCTURE, NEW_REVIEW_STRUCTURE, UPDATE_BUSINESS_STRUCTURE
from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers

log = logging.getLogger(__name__)

ns = api.namespace(
    'businesses',
     description='Operations related to Businesses')

init_we_connect_users = WeConnectUsers()


@ns.route('/')
class RegisterBusiness(Resource):

    @ns.expect(NEW_BUSINESS_STRUCTURE, code=201)
    @api.doc(security='apikey')
    @token_required
    def post(self):
        """
        Register a business.
        """
        return init_we_connect_users.create_business(api.payload)

    @api.doc(security='apikey')
    @token_required
    def get(self):
        """
        Retrieves all businesses.
        """
        return init_we_connect_users.show_all_businesses()


@ns.route('/<int:business_id>')
@ns.response(404, 'Business not found')
class ShowBusiness(Resource):

    @api.doc(security='apikey')
    @token_required
    def get(self, business_id):
        """
        Get a business.
        """
        return init_we_connect_users.show_business_by_business_id(business_id)

    @ns.response(204, 'Business deleted')
    @api.doc(security='apikey')
    @token_required
    def delete(self, business_id):
        """
        Remove a business.
        """
        return init_we_connect_users.delete_business_by_business_id(business_id)


    @ns.expect(UPDATE_BUSINESS_STRUCTURE, code=201)
    @api.doc(security='apikey')
    @token_required
    def put(self, business_id):
        """
        Updates a business profile.
        """
        return init_we_connect_users.update_business_by_business_id(business_id, api.payload)


@ns.route('/<int:business_id>/reviews')
class BusinessReviews(Resource):

    @api.doc(security='apikey')
    @token_required
    @ns.expect(NEW_REVIEW_STRUCTURE, code=201)
    def post(self, business_id):
        """
        Add a review for a business.
        """
        return init_we_connect_users.add_review_to_businesss(business_id, api.payload)

    @api.doc(security='apikey')
    @token_required
    def get(self, business_id):
        """
        Get all reviews for a business.
        """
        return init_we_connect_users.view_business_reviews(business_id)