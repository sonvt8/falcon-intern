from falcon import testing
from main import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_tc01(self):
        INPUT_name = '123'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code != 200

    def test_tc02(self):
        INPUT_name = 'a!bc'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code != 200

    def test_tc03(self):
        INPUT_name = 'some name'
        r = self.simulate_get(f'/hello/{INPUT_name}')
        assert r.status_code == 200
        assert r.text == f'Hello {INPUT_name}'


