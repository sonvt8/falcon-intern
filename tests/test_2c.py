from falcon import testing
import json
from main_2b import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api


    def test_tc00(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname':'', 'lname': ''}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values cannot be empty' in e

    def test_tc0a(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': 'abc', 'lname': ''}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values cannot be empty' in e


    def test_tc01(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': '123', 'lname': '@#$'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values ​​must be valid' in e

    def test_tc01a(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': '', 'lname': '@#$'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all values ​​must be valid' in e


    def test_tc02(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'': 'abc', '': 'abc'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all key cannot be empty' in e

    def test_tc02a(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': 'abc', '': 'abc'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'all key cannot be empty' in e


    def test_tc03(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'not_fname': 'abc', 'not_lname': 'abc'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'key must be fname and lname' in e

    def test_tc03a(self):
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': 'abc', 'not_lname': 'abc'}))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'key must be fname and lname' in e


    def test_tc04(self):
        first_name = 'some first name'
        last_name = 'some last name'
        r = self.simulate_post(f'/hello/', body=json.dumps({'fname': {first_name},'lname': {last_name}}))
        expected_out = json.dumps({'message': f'hello {first_name} {last_name}'})
        assert r.status_code == 200
        assert r.text == expected_out

