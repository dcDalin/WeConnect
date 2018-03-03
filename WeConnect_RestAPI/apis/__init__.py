from flask_restplus import Api

from .namespace1 import api as ns1
from .namespace2 import api as ns2

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns1, path='/prefix/of/ns1')
api.add_namespace(ns2, path='/prefix/of/ns2')