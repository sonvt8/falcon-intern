import falcon
import json
from .model import *
from falcon_autocrud.middleware import Middleware

# helper to convert object including timestamp into JSON
def convert_timestamp(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

# get customer info as a dictionary
def customer_info(o):
    if not o:
        return {}

    info = {
        'id'        : o.id,
        'name'      : o.name,
        'dob'       : o.dob,
        'updated_at': o.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

# READ
class CustomerResource:
    def on_get(self, req, resp):
        customers = db.session.query(Customer)
        lst_customer = []
        for customer in customers:
            lst_customer.append(customer_info(customer))
        resp.body = json.dumps(lst_customer, default=convert_timestamp)

    def on_post(self, req, resp):
        body = req.media

        name = body.get('name')
        if not name:
            raise falcon.HTTPBadRequest(title='Data param name is required', description='Problem when process request')

        dob = body.get('dob')
        if not dob:
            raise falcon.HTTPBadRequest(title='Data param dob is required', description='Problem when process request')

        new_customer = Customer(name, dob)
        db.session.add(new_customer)
        db.session.flush()
        db.session.commit()
        resp.body = json.dumps({'id': f'{new_customer.id}'})


class SingleReadResource:

    def on_get(self, req, resp,id):
        customer = db.session.query(Customer).get(id)
        resp.body = json.dumps(customer_info(customer), default=convert_timestamp)

# ------- Add route ------
api = falcon.API()
# api = application = falcon.API(middleware=[Middleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/customers', CustomerResource())
api.add_route('/customers/{id}', SingleReadResource())
