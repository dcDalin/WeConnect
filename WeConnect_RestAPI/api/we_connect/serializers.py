from flask_restplus import fields
from WeConnect_RestAPI.api.restplus import api

NEW_USER_STRUCTURE = api.model('User', {
    'first_name': fields.String(required=False, description='First name of a User'),
    'last_name': fields.String(required=False, description='Last name of a User'),
    'email': fields.String(required=False, description='Email address of a User'),
    'gender': fields.String(required=False, description='Gender of a User', enum=['Male', 'Female', 'Other']),
    'password': fields.String(required=False, description='The password of a User'),
})

LOGIN_STRUCTURE = api.model('Login User', {
    'email': fields.String(required=True, description='Email address of a User'),
    'password': fields.String(required=True, description='The password of a User'),
})

logout_structure = api.model('Logout User', {
    'token': fields.String(required=True, description='Logout token')
})

reset_pass_structure = api.model('Reset User Password', {
    'email': fields.String(required=True, description='Email address of a User'),
    'password': fields.String(required=True, description='The password of a User'),
})