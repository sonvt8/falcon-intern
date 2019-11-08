from falcon import testing
import json
from Customer.app_noAuto import api
from Customer.model import *


def setUpModule(): pass  # nothing here for now


def tearDownModule(): pass  # nothing here for now


def createFixture():
    db.engine.execute('DROP TABLE IF EXISTS customers;')
    db.engine.execute('''
        CREATE TABLE customers(
            id           serial PRIMARY KEY,
            name         varchar (50),
            dob          date,
            updated_at    timestamp 
        );
    ''')
    faker_data()

class Test(testing.TestCase):

    def setUp(self):
        # Create text fixtures
        createFixture()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        r = self.simulate_get('/customers')
        assert r
        assert r.json == [
            {'id': 1, 'name': 'Václav Beneš',           'dob': '1994-06-25', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 2, 'name': 'Jitka Vávrová',          'dob': '2007-12-27', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 3, 'name': 'Stanislava Růžičková',   'dob': '1998-07-06', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 4, 'name': 'Romana Křížová',         'dob': '2007-08-01', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 5, 'name': 'Ondřej Kratochvíl',      'dob': '2009-10-26', 'updated_at': '2019-11-07 23:31:40'},
        ]

    def test_01(self):
        r = self.simulate_get('/customers/4')
        assert r
        assert r.json == {'id': 4, 'name': 'Romana Křížová', 'dob': '2007-08-01', 'updated_at': '2019-11-07 23:31:40'}

    def test_02(self):
        r = self.simulate_get('/customers/7')
        assert r.json == {}


class TestPOST(testing.TestCase):

    def setUp(self):
        createFixture()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        new_customer = {
            "name"	: "Binh Vu",
            "dob"	: "1993-07-13"
        }
        r = self.simulate_post(f'/customers', body=json.dumps(new_customer))
        assert r
        assert r.json == {'id': f'6'}


