import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.business import WeConnect
from WeConnect_RestAPI.api.we_connect.serializers import new_user_structure, login_structure, logout_structure, reset_pass_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('auth', description='Operations related to Authentication')


@ns.route('/register')
class RegisterUser(Resource):

    @api.expect(new_user_structure)
    def post(self):
        """
        Creates a user account.
        """
        pass

@ns.route('/login')
class LoginUser(Resource):
    
    @api.expect(login_structure)
    def post(self):
        """
        Logs in a User.
        """
        pass

@ns.route('/logout')
class LoginUser(Resource):
    
    @api.expect(logout_structure)
    def post(self):
        """
        Logs out a User.
        """
        pass

@ns.route('/reset-password')
class LoginUser(Resource):
    
    @api.expect(reset_pass_structure)
    def post(self):
        """
        Resets User password.
        """
        pass