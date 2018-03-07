import logging.config

from flask import Flask, Blueprint
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from WeConnect_RestAPI import settings
from WeConnect_RestAPI.api.we_connect.endpoints.auth import ns as auth_namespace
from WeConnect_RestAPI.api.we_connect.endpoints.businesses import ns as businesses_namespace
from WeConnect_RestAPI.api.restplus import api

app = Flask(__name__)
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SECRET_KEY'] = settings.SECRET_KEY
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    flask_app.config['SWAGGER_UI_JSONEDITOR'] = settings.SWAGGER_UI_JSONEDITOR
    flask_app.config[
        'SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(auth_namespace)
    api.add_namespace(businesses_namespace)
    flask_app.register_blueprint(blueprint)
    return flask_app


def main(app):
    app = initialize_app(app)
    jwt = JWTManager(app)
    log.info(
        '>>>>> Starting development server at http://{}/api/v1 <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)

if __name__ == "__main__":
    main(app)
