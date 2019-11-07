from Customer.database import Database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
import datetime

# Make a connection to database
db = Database()
Base = declarative_base()


# Creat a class Customer
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)  # Auto-increment should be default autoincrement=True
    name = Column(String)
    dob = Column(Date)
    updated_at = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

def faker_data():
    faker = Faker('cz_CZ')
    for i in range(1, 6):
        name = faker.name()
        dob= faker.date_time_between(start_date='-30y', end_date='now')
        new_customer = Customer (name,dob)
        db.session.add(new_customer)
        db.session.commit()

if __name__ == '__main__':
    # Drop table customers if existed before
    Base.metadata.drop_all(db.engine)
    # Create new table customers
    Base.metadata.create_all(db.engine)
    faker_data()


