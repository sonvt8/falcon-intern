import falcon

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


app = falcon.API()
app.add_route('/health', HealthResource())
app.add_route('/hello/{name}', HelloResource())
# any other route should be placed before the handle_404 one
app.add_sink(handle_404, '')

