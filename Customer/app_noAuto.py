import falcon
import json
from .model import *


# helper to convert object including timestamp into JSON
def convert_timestamp(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


# get customer info as a dictionary
def customer_info(o):
    if not o:
        return {}

    info = {
        'id': o.id,
        'name': o.name,
        'dob': o.dob,
        'updated_at': o.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    }
    return info


class CustomerResource:
    # CREATE
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

    # READ ALL
    def on_get(self, req, resp):
        customers = db.session.query(Customer)
        lst_customer = []
        for customer in customers:
            lst_customer.append(customer_info(customer))
        resp.body = json.dumps(lst_customer, default=convert_timestamp)

class SingleReadResource:
    # READ WITH ID
    def on_get(self, req, resp, id):
        customer = db.session.query(Customer).get(id)
        resp.body = json.dumps(customer_info(customer), default=convert_timestamp)

    # UPDATE
    def on_put(self, req, resp, id):
        body = req.media
        name = body.get('name')
        dob = body.get('dob')
        flag = 0
        customers = db.session.query(Customer)

        for customer in customers:
            if int(id) is customer.id:
                if name:
                    customer.name = name
                if dob:
                    customer.dob = dob
                customer.updated_at = datetime.datetime.now()
                db.session.commit()
                flag = 1
                break

        if flag == 1:
            customer = db.session.query(Customer).get(id)
            resp.body = json.dumps(customer_info(customer), default=convert_timestamp)
        else:
            resp.body = f'id = {id} not found'

    def on_delete(self, req, resp, id):
        customer = db.session.query(Customer).get(id)
        resp.body = json.dumps(customer_info(customer), default=convert_timestamp)
        db.session.delete(customer)
        db.session.commit()

# ------- Add route ------
api = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/customers', CustomerResource())
api.add_route('/customers/{id}', SingleReadResource())
