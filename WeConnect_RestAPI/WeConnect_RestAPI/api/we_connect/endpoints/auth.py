import logging

from flask import request
from flask_restplus import Resource
from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers
from WeConnect_RestAPI.api.we_connect.serializers import NEW_USER_STRUCTURE, login_structure, logout_structure, reset_pass_structure
from WeConnect_RestAPI.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('auth', description='Operations related to Authentication')

initWeConnectUsers = WeConnectUsers()

@ns.route('/register')
class RegisterUser(Resource, WeConnectUsers):

    @api.doc(responses={403: 'Not Authorized', 404: 'Not Found', 201: 'User added', 400: 'Bad request'})
    #@api.expect(NEW_USER_STRUCTURE, validate=True, code=201)
    def post(self):
        """
        Creates a user account.
        """ 
        return initWeConnectUsers.create_user(api.payload)
    
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

@ns.route('/all-users')
class ShowAllUsers(Resource, WeConnectUsers):
    
    def get(self):
        """
        Returns all users.
        """
        return initWeConnectUsers.show_all_users()