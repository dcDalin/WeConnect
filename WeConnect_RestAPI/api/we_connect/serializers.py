from flask_restplus import fields
from WeConnect_RestAPI.api.restplus import api

NEW_USER_STRUCTURE = api.model('User', {
    'first_name': fields.String(
    required=False,
    description='First name of a User'),
    'last_name': fields.String(
        required=False,
        description='Last name of a User'),
    'email': fields.String(
        required=False,
        description='Email address of a User'),
    'gender': fields.String(
        required=False,
        description='Gender of a User',
     enum=['Male',
           'Female',
           'Other']),
    'password': fields.String(
        required=False,
        description='The password of a User'),
})

LOGIN_STRUCTURE = api.model('Login User', {
    'email': fields.String(
        required=True,
        description='Email address of a User'),
        'password': fields.String(
        required=True,
        description='The password of a User'),
})

RESET_PASSWORD_STRUCTURE = api.model('Reset Password', {
    'password': fields.String(
        required=True,
        description='The password of a User'),
})

NEW_BUSINESS_STRUCTURE = api.model('Business', {
    'business_name': fields.String(
    required=True,
    description='The name of a Business'),
    'business_category': fields.String(
        required=True,
        description='Category of a Business',
     enum=['Service',
           'Merchandising',
           'Manufacturing']),
    'business_email': fields.String(
        required=True,
        description='Email address of a Business'),
    'business_description': fields.String(
        required=True,
        description='The description of a Business'),
    'business_phone': fields.String(
        required=True,
        description='Phone number address of a Business'),
})


UPDATE_BUSINESS_STRUCTURE = api.model('Update Business', {
    'business_name': fields.String(
    required=True,
    description='The name of a Business'),
    'business_category': fields.String(
        required=True,
        description='Category of a Business',
     enum=['Service',
           'Merchandising',
           'Manufacturing']),
    'business_description': fields.String(
        required=True,
        description='The description of a Business'),
})


NEW_REVIEW_STRUCTURE = api.model('Review', {
    'review_message': fields.String(
    required=True,
    description='The Review'),
    'review_rating': fields.String(
        required=True,
        description='Rating of the Review',
     enum=['1',
           '2',
           '3',
           '4',
           '5']),
})


logout_structure = api.model('Logout User', {
    'token': fields.String(required=True, description='Logout token')
})