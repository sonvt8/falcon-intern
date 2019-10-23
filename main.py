import falcon
import datetime

now = datetime.datetime.now()  #TODO khai bao ngay gan` code su dung; ko can phai toan cuc

#tc00
class HealthResource:
    def on_get(self, req, resp):
        resp.body = 'Hello'  #TODO sai yeu cau, chi can tra ve 200, body rong~

def handle_404(req, resp):  #TODO khai bao gan .add_sink()
    resp.status = falcon.HTTP_404  #TODO khi loi~ khong fai la 404 thi sao?
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
app.add_sink(handle_404, '')  #TODO code nay tuyet voi!

