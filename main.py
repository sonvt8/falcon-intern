import falcon
import datetime

#tc00
class HealthResource:
    def on_get(self, req, resp):
        resp.body = ''

# tc1b
class HelloResource:
    def on_get(self, req, resp, name):
        resp.body = f'Hello {name}'

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


api = falcon.API()
api.add_route('/health', HealthResource())
api.add_route('/hello/{name}', HelloResource())
api.add_route('/hi', HiResource())

def handle_404(req, resp):
    # urllib.getcode()
    resp.status = falcon.HTTP_CONFLICT #TODO khi loi~ khong fai la 404 thi sao? -->
    resp.body = 'Not found'
# any other route should be placed before the handle_404 one
api.add_sink(handle_404, '')