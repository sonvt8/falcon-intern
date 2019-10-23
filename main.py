import falcon
import datetime

now = datetime.datetime.now()

#tc00
class HealthResource:
    def on_get(self, req, resp):
        resp.body = 'Hello'

def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = 'Not found'

# tc1b
class HelloResource:
    def on_get(self, req, resp, name):
        resp.body = f'Hello {name}'

# tc1a
class HiResource:
    def on_get(self, req, resp):
        if 0 <= int(now.hour) <= 11:
            resp.body = f'Good morning'
        elif 12 <= int(now.hour) <= 17:
            resp.body = f'Good afternoon'
        else:
            resp.body = f'Good evening'

app = falcon.API()
app.add_route('/health', HealthResource())
app.add_route('/hello/{name}', HelloResource())
app.add_route('/hi', HiResource())

# any other route should be placed before the handle_404 one
app.add_sink(handle_404, '')

