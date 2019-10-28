from falcon import testing
import json
from main_JSON import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        r = self.simulate_get('/health')
        assert r.status_code == 200

    def test_01a(self):
        r = self.simulate_get(f'/hi')
        assert r.status_code == 200
        expected_out = json.dumps({'output':'Good afternoon'})
        assert r.text == expected_out

    def test_01b_tc01(self):
        INPUT_name = '1!a3'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code != 200

    def test_01b_tc02(self):
        INPUT_name = 'some name'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code == 200
        expected_out = json.dumps({'output': f'Hello {INPUT_name}'})
        assert r.text == expected_out

    def test_01c_valid(self):
        INPUT_name = 'some name'
        r = self.simulate_get(f'/hola/{INPUT_name}')
        assert r.status_code == 200
        expected_out = json.dumps({'output': f'Hola {INPUT_name}'})
        assert r.text == expected_out

    def test_01c_empty(self):
        INPUT_name = ''
        r = self.simulate_get(f'/hola/{INPUT_name}')
        assert r.status_code != 200
        e = r.json.get('title');
        assert e  # e aka exception
        assert 'name is required' in e

    def test_not_valid(self):
        INPUT_name = '1!23'
        r = self.simulate_get(f'/hola/{INPUT_name}')
        assert r.status_code != 200
        e = r.json.get('title');
        assert e  # e aka exception
        assert 'name must be a valid string' in e







