import logging
import traceback

from flask_restplus import Api
from WeConnect_RestAPI import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='We Connect API',
          description='Documentation of We Connect API')