from .database import Database
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

# Make a connection to database
db = Database()
Base = declarative_base()


# Creat a class Customer
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)  # Auto-increment should be default autoincrement=True
    name = Column(String)
    birth = Column(Date)
    address = Column(String(50))
    phone = Column(String(20))

    def __init__(self, name, birth, address, phone):
        self.name = name
        self.birth = birth
        self.address = address
        self.phone = phone

def faker_data():
    faker = Faker('cz_CZ')
    for i in range(1, 5):
        name = faker.name()
        birth = faker.date_time_between(start_date='-30y', end_date='now')
        address = faker.address()
        phone = faker.phone_number()
        new_customer = Customer (name,birth,address,phone)
        db.session.add(new_customer)
        db.session.commit()

if __name__ == '__main__':
    # Drop table customers if existed before
    Base.metadata.drop_all(db.engine)
    # Create new table customers
    Base.metadata.create_all(db.engine)
    faker_data()


