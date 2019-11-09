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
            name         varchar (50) NOT NULL,
            dob          date,
            updated_at    timestamp 
        );
    ''')
    db.engine.execute('''
        INSERT INTO customers (name, dob, updated_at)
        VALUES
            ('Thai Son'    , '1988-05-15', '2019-11-07 23:31:40'),
            ('Thai Binh'   , '1993-07-13', '2019-11-07 23:31:40'),
            ('Minh Anh'    , '1982-01-01', '2019-11-07 23:31:40'),
            ('Name04'      , '2011-12-01', '2019-11-07 23:31:40'),
            ('Name05'      , '2018-05-06', '2019-08-16 08:09:01')
    ''');

class Test(testing.TestCase):

    def setUp(self):
        # Create text fixtures
        createFixture()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_03(self):
        r = self.simulate_get('/customers')
        assert r
        assert r.json == [
            {'id': 1, 'name': 'Thai Son'    , 'dob': '1988-05-15', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 2, 'name': 'Thai Binh'   , 'dob': '1993-07-13', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 3, 'name': 'Minh Anh'    , 'dob': '1982-01-01', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 4, 'name': 'Name04'      , 'dob': '2011-12-01', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 5, 'name': 'Name05'      , 'dob': '2018-05-06', 'updated_at': '2019-08-16 08:09:01'}
        ]

    def test_03a(self):
        r = self.simulate_get('/customers/5')
        assert r
        assert r.json == {'id': 5, 'name': 'Name05'      , 'dob': '2018-05-06', 'updated_at': '2019-08-16 08:09:01'}

    def test_03b(self):
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

    def test_tc01(self):
        new_customer = {
            "name"	: "Binh Vu"
        }
        r = self.simulate_post(f'/customers', body=json.dumps(new_customer))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'Data param dob is required' in e

    def test_tc02(self):
        new_customer = {
            "dob"	: "1993-07-13"
        }
        r = self.simulate_post(f'/customers', body=json.dumps(new_customer))
        assert r.status_code != 200
        e = r.json.get('title'); # e aka exception
        assert 'Data param name is required' in e


class TestPUT(testing.TestCase):

    def setUp(self):
        createFixture()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_04(self):
        new_customer = {
            "name"	: "Son"
        }
        r = self.simulate_put(f'/customers/3', body=json.dumps(new_customer))
        assert r
        # NOTE: Comment datetime.now() in on_put method of app_noAuto.py before doing unittest
        assert r.json == {'id': 3, 'name': 'Son', 'dob': '1982-01-01', 'updated_at': '2019-11-07 23:31:40'}

    def test_04a(self):
        new_customer = {
            "dob": "2011-11-11"
        }
        r = self.simulate_put(f'/customers/4', body=json.dumps(new_customer))
        assert r
        # NOTE: Comment datetime.now() in on_put method of app_noAuto.py before doing unittest
        assert r.json == {'id': 4, 'name': 'Name04', 'dob': '2011-11-11', 'updated_at': '2019-11-07 23:31:40'}


class TestDELETE(testing.TestCase):

    def setUp(self):
        createFixture()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_05(self):
        r = self.simulate_delete('/customers/2')
        assert r
        assert r.json == {'id': 2}

