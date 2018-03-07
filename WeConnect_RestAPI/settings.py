# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production
SECRET_KEY = 'random2389'
JWT_SECRET_KEY = 'crazysecret'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
SWAGGER_UI_JSONEDITOR = True
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
