import falcon
import datetime
import re
import json

# ------- Define handling method------
def verify(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
    if (regex.search(string) == None):
        return True
    else:
        return False

#  test 2b
def get_name(my_str):
    lst_str = my_str.lstrip('/').split('/')
    return " ".join(lst_str)

#  Test 2a
class HealthResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = (json.dumps({"output": ""}))

class HiResource:
    def on_get(self, req, resp):
        now = datetime.datetime.now()
        if 0 <= int(now.hour) <= 11:
            resp.body = (json.dumps({"output": "Good morning"}))
        elif 12 <= int(now.hour) <= 17:
            resp.body = (json.dumps({"output": "Good afternoon"}))
        else:
            resp.body = (json.dumps({"output": "Good everning"}))

class HelloResource:
    def on_get(self, req, resp, name):
        if verify(name) is False:
            resp.status = falcon.HTTP_404
        else:
            resp.body = (json.dumps({"output": f'Hello {name}'}))

class HolaResource:
    def on_get(self, req, resp, name):
        if verify(name) is False:
            raise falcon.HTTPBadRequest(title='name must be a valid string', description='Problem when process request')
        else:
            resp.body = (json.dumps({"output": f'Hola {name}'}))

# test 2c
class IndexResource:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = req.params['fname']

# test 2d
class StaticResource(object):
    def on_get(self, req, resp):
        csv_file_path = "test.csv"
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/csv'
        with open(csv_file_path, 'r') as f:
            resp.body = f.read()

# ------- Add route ------
api = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hi', HiResource())
api.add_route('/hola/{name}', HolaResource())
api.add_route('/hellopost', IndexResource())
api.add_route('/readcsv', StaticResource())

# ------- Define method to handle Sink ------
def hola(req, resp):
    raise falcon.HTTPBadRequest(title='name is required', description='Problem when process request')

def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = 'Not found'

# def hello(req, resp):
#     url = req.relative_uri
#     resp.body = json.dumps({"output": get_name(url)})

# ------- Add sink like a router ------
api.add_sink(handle_404, '')
api.add_sink(hola, '/hola')
# api.add_sink(hello, '/hello')
