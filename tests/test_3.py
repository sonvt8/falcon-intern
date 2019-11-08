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

def createFixture_get():
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
            ('Thanh Nguyen', '1985-12-04', '2019-11-07 23:31:40'),
            ('Duc Nguyen'  , '1997-10-03', '2019-11-07 23:31:40')
    ''');

class Test(testing.TestCase):

    def setUp(self):
        # Create text fixtures
        createFixture_get()

    def tearDown(self): pass  # nothing here for now

    app = api

    def test_00(self):
        r = self.simulate_get('/customers')
        assert r
        assert r.json == [
            {'id': 1, 'name': 'Thai Son'    , 'dob': '1988-05-15', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 2, 'name': 'Thai Binh'   , 'dob': '1993-07-13', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 3, 'name': 'Minh Anh'    , 'dob': '1982-01-01', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 4, 'name': 'Thanh Nguyen', 'dob': '1985-12-04', 'updated_at': '2019-11-07 23:31:40'},
            {'id': 5, 'name': 'Duc Nguyen'  , 'dob': '1997-10-03', 'updated_at': '2019-11-07 23:31:40'}
        ]

    def test_01(self):
        r = self.simulate_get('/customers/4')
        assert r
        assert r.json == {'id': 4, 'name': 'Thanh Nguyen', 'dob': '1985-12-04', 'updated_at': '2019-11-07 23:31:40'}

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