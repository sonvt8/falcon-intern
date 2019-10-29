from falcon import testing
import json
from main_JSON import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api


    def test_tc00(self):
        r = self.simulate_get(f'/hello/')
        assert r.status_code != 200
        e = r.json.get('title');
        assert e  # e aka exception
        assert 'Params are required' in e

    def test_tc01(self):
        first_name = 'abc'
        r = self.simulate_get(f'/hello/{first_name}')
        assert r.status_code != 200
        e = r.json.get('title');
        assert e  # e aka exception
        assert 'All params are required' in e

    def test_tc02(self):
        first_name = '123'
        last_name = '@#$'
        r = self.simulate_get(f'/hello/{first_name}/{last_name}')
        assert r.status_code != 200
        e = r.json.get('title');
        assert e  # e aka exception
        assert 'All params must be valid' in e

    def test_tc03(self):
        first_name = 'son'
        last_name = 'vu'
        r = self.simulate_get(f'/hello/{first_name}/{last_name}')
        assert r.status_code == 200
        expected_out = json.dumps({'output': f'hello {first_name} {last_name}'})
        assert r.text == expected_out

