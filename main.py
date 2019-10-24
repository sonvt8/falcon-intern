import falcon
import datetime
import re


def verify(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')

    # Pass the string in search
    # method of regex object.
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
        resp.body = f'Hello {name}'


# tc1c
class HolaResource:
    def on_get(self, req, resp, name):
        if name == '':
            resp.body = f'name is required'
        elif verify(name) is False:
            resp.body = f'name must be a valid string'
        else:
            resp.body = f'Hola {name}'


api = falcon.API()
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hi', HiResource())
api.add_route('/hola/{name}', HolaResource())


def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = 'Link not found'


# any other route should be placed before the handle_404 one
api.add_sink(handle_404, '')
