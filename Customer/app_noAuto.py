import falcon
import json
from .model import *
from falcon_autocrud.middleware import Middleware

# helper to convert object including timestamp into JSON
def convert_timestamp(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

# CREATE
class AddResource:
    def on_post(self, req, resp):
        output = req.media
        new_customer = Customer (output['name'], output['dob'])
        db.session.add(new_customer)
        db.session.commit()
        resp.body = 'Create new customer successfully'

# READ
class ReadResource:
    def on_get(self, req, resp):
        customers = db.session.query(Customer)
        lst_customer = []
        for customer in customers:
            customer_info = {
                'id'        :   customer.id,
                'name'      :   customer.name,
                'dob'       :   customer.dob,
                'updated_at':   customer.updated_at.strftime("%Y-%m-%d %H:%M:%S")
            }
            lst_customer.append(customer_info)
        resp.body = json.dumps(lst_customer, default=convert_timestamp)


# ------- Add route ------
api = application = falcon.API(middleware=[Middleware()])
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/customers', ReadResource())