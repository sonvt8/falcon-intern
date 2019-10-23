import falcon

#tc00
class HealthResource:
    def on_get(self, req, resp):
        resp.body = 'Hello'

def handle_404(req, resp):
    resp.status = falcon.HTTP_404
    resp.body = 'Not found'

app = falcon.API()
app.add_route('/', HealthResource())
# any other route should be placed before the handle_404 one
app.add_sink(handle_404, '')