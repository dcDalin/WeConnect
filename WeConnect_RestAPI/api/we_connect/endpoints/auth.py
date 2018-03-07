import logging

from flask import request, Blueprint
from flask_restplus import Resource
from functools import wraps
from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers
from WeConnect_RestAPI.api.we_connect.serializers import (NEW_USER_STRUCTURE, 
    LOGIN_STRUCTURE, logout_structure, reset_pass_structure)
from WeConnect_RestAPI.api.restplus import api 

log = logging.getLogger(__name__)

ns = api.namespace('auth', description='Operations related to Authentication')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401
 
        if token != 'mytoken':
            return {'message' : 'Wrong token'}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated

init_we_connect_users = WeConnectUsers()

@ns.route('/register')
class RegisterUser(Resource, WeConnectUsers):

    @api.doc(responses={403: 'Not Authorized', 404: 'Not Found'})
    @api.expect(NEW_USER_STRUCTURE, validate=True, code=201)
    def post(self):
        """
        Creates a user account.
        """ 
        return init_we_connect_users.create_user(api.payload)
    
@ns.route('/login')
class LoginUser(Resource):
    
    @api.expect(LOGIN_STRUCTURE)
    def post(self):
        """
        Logs in a User.
        """
        return init_we_connect_users.login_user(api.payload)

@ns.route('/logout')
class LogOut(Resource):
    
    @api.doc(security='apikey')
    def post(self):
        """
        Logs out a User.
        """
        pass

@ns.route('/reset-password')
class ResetPassword(Resource):
    
    @api.expect(reset_pass_structure)
    def post(self):
        """
        Resets User password.
        """
        pass

@ns.route('/all-users')
class ShowAllUsers(Resource, WeConnectUsers):
    
    
    @api.doc(security='apikey')
    @token_required
    def get(self):
        """
        Returns all users.
        """
        return init_we_connect_users.show_all_users()
