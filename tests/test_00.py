from falcon import testing
from main import api


def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(testing.TestCase):

    def setUp(self):    pass  # nothing here for now
    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        r = self.simulate_get('/health')
        assert r.status_code == 200
