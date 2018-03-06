from flask_restplus import fields
from WeConnect_RestAPI.api.restplus import api

NEW_USER_STRUCTURE = api.model('User', {
    'firstName': fields.String(required=False, description='First name of a User'),
    'lastName': fields.String(required=False, description='Last name of a User'),
    'email': fields.String(required=False, description='Email address of a User'),
    'gender': fields.String(required=False, description='Gender of a User', enum=['Male', 'Female', 'Other']),
    'password': fields.String(required=False, description='The password of a User'),
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

NEW_BUSINESS_STRUCTURE = api.model('Business', {
    'businessName': fields.String(required=True, description='The name of a Business'),
    'businessCategory': fields.String(required=True, description='Category of a Business', enum=['Service', 'Merchandising', 'Manufacturing']),
    'businessEmail': fields.String(required=True, description='Email address of a Business'),
})

view_business_structure = api.model('View Business', {
    'businessId': fields.Integer(readOnly=True, description='The business unique identifier'),
    'businessName': fields.String(required=True, description='The name of a Business'),
    'businessCategory': fields.String(required=True, description='Category of a Business'),
    'businessEmail': fields.String(required=True, description='Email address of a Business'),
    'date_created': fields.DateTime,
})