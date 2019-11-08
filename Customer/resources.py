from falcon_autocrud.resource import CollectionResource, SingleResource
from .model import *
import falcon

class customerCollectionResource(CollectionResource):
    model = Customer

    def before_post(self, req, resp, db_session, resource, *args, **kwargs):
        if resource.name == '':
            raise falcon.HTTPBadRequest(title='Data param name is required', description='Problem when process request')
        if resource.dob == '':
            raise falcon.HTTPBadRequest(title='Data param dob is required', description='Problem when process request')

    def after_post(self, req, resp, new, *args, **kwargs):
        resp.status = falcon.HTTP_200


class customerResource(SingleResource):
    model = Customer
