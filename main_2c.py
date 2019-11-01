import falcon
import re
import json

# ------- Define handling method------
def verify(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')
    if regex.search(string) is None:
        return True
    else:
        return False

# test 2c
class IndexResource:
    def on_post(self, req, resp):
        output = req.media
        fname = output['fname']
        lname  = output['lname']

        if fname == '' or lname == '':
            raise falcon.HTTPBadRequest(title='all values cannot be empty', description='Problem when process request')
        elif verify(fname) is False or verify(lname) is False:
            raise falcon.HTTPBadRequest(title='all values ​​must be valid', description='Problem when process request')
        else:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({
                'message': f'Hello {fname} {lname}'
            })

# ------- Add route ------
api = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
api.add_route('/hello/', IndexResource())
