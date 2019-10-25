import falcon
import datetime
import re

def verify(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
    if (regex.search(string) == None):
        return True
    else:
        return False

# tc00
class HealthResource:
    def on_get(self, req, resp):
        resp.body = ''

# tc1a
class HiResource:
    def on_get(self, req, resp):
        now = datetime.datetime.now()
        if 0 <= int(now.hour) <= 11:
            resp.body = f'Good morning'
        elif 12 <= int(now.hour) <= 17:
            resp.body = f'Good afternoon'
        else:
            resp.body = f'Good evening'

# tc1b
class HelloResource:
    def on_get(self, req, resp, name):
        if verify(name) is False:
            resp.status = falcon.HTTP_404
        else:
            resp.body = f'Hello {name}'

# tc1c
class HolaResource:
    def on_get(self, req, resp, name):
        # url = req.url
        # url_parts = url.rsplit("/", 1)
        # resp.body = url_parts[1]
        if verify(name) is False:
            raise falcon.HTTPBadRequest(title='name must be a valid string',description='Problem when process request')
        else:
            resp.body = f'Hola {name}'

api = falcon.API()
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hi', HiResource())
api.add_route('/hola/{name}', HolaResource())

def hola(req, resp):
    raise falcon.HTTPBadRequest(title='name is required', description='Problem when process request')

def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = 'Not found'

api.add_sink(handle_404, '')
api.add_sink(hola, '/hola')
