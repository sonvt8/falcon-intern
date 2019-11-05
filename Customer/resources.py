from falcon_autocrud.resource import CollectionResource, SingleResource
from .model import *


class customerCollectionResource(CollectionResource):
    model = Customer


class customerResource(SingleResource):
    model = Customer
