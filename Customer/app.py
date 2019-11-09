from .resources import *

# ------- Add route ------
api = falcon.API()
# api.req_options.auto_parse_form_urlencoded = True
api.add_route('/customers', CustomerResource())
api.add_route('/customers/{id}', SingleResource())
