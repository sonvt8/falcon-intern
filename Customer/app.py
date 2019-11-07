from falcon_autocrud.middleware import Middleware
from .resources import *

api = application = falcon.API(middleware=[Middleware()])
api.add_route('/customers', customerCollectionResource(db.engine))
api.add_route('/customers/{id}', customerResource(db.engine))
