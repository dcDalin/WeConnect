from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask_restplus import Api, Resource, fields
from functools import wraps 
from WeConnect_RestAPI.api.we_connect.custom_validation import is_empty
from WeConnect_RestAPI.api.we_connect.business import WeConnectUsers

init_we_connect_users = WeConnectUsers()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']

        if not token:
            return {'message' : 'Token is missing.'}, 401

        token = request.headers['X-API-KEY']
        if token != init_we_connect_users.current_logged_in_user():
            return {"message": "Wrong token"}, 401

        print('TOKEN: {}'.format(token))
        return f(*args, **kwargs)

    return decorated