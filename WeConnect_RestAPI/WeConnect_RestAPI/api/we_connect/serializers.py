from flask_restplus import fields
from WeConnect_RestAPI.api.restplus import api

new_user_structure = api.model('User', {
    '_id': fields.Integer(readOnly=True, description='The unique identifier of a User'),
    'first_name': fields.String(required=True, description='First name of a User'),
    'last_name': fields.String(required=True, description='Last name of a User'),
    'email': fields.String(required=True, description='Email address of a User'),
    'password': fields.String(required=True, description='The password of a User'),
    'date_created': fields.DateTime,
})

login_structure = api.model('Login User', {
    'email': fields.String(required=True, description='Email address of a User'),
    'password': fields.String(required=True, description='The password of a User'),
    'last_login': fields.DateTime,
})

logout_structure = api.model('Logout User', {
    'token': fields.String(required=True, description='Logout token')
})

reset_pass_structure = api.model('Reset User Password', {
    'email': fields.String(required=True, description='Email address of a User'),
    'password': fields.String(required=True, description='The password of a User'),
})

new_business_structure = api.model('Business', {
    'businessName': fields.String(required=True, description='Name of a Business'),
    'businessCategory': fields.String(required=True, description='Category of a Business'),
    'businessEmail': fields.String(required=True, description='Email address of a Business'),
    'date_created': fields.DateTime,
})