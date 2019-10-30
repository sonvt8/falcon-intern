import falcon
import re
import json

# ------- Define handling method ------
def verify(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
    if (regex.search(string) == None):
        return True
    else:
        return False

def get_index(my_str):
    lst_str = my_str.lstrip('/').split('/')
    return len(lst_str)

# ------- main task ------
class HelloResource:
    def on_get(self, req, resp, first_name, last_name):
        if verify(first_name) is False or verify(last_name) is False:
            raise falcon.HTTPBadRequest(title='All params must be valid', description='Problem when process request')
        else:
            resp.body = (json.dumps({"output": f'hello {first_name} {last_name}'}))

# ------- Exception ------
def hello(req, resp):
    url = req.path
    if get_index(url) == 1:
        raise falcon.HTTPBadRequest(title='Params are required', description='Problem when process request')
    elif get_index(url) == 2:
        raise falcon.HTTPBadRequest(title='All params are required', description='Problem when process request')
    else:
        raise falcon.HTTPBadRequest(title='URL should not include more than two params', description='Problem when process request')

# ------- Add route ------
api = falcon.API()
api.add_route('/hello/{first_name}/{last_name}', HelloResource())

# ------- Add sink like a router ------
api.add_sink(hello, '/hello')