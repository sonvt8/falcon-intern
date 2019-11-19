--00 Find what activities are taking place
SELECT * FROM pg_stat_activity WHERE datname = 'customer_api';

--01 terminate the connection
SELECT pg_terminate_backend (pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'customer_api';

--03 Drop and Create Database
DROP DATABASE customer_api;
CREATE DATABASE customer_api;
\c customer_api;

--04 Create Table
DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
    id          serial PRIMARY KEY,
    name        varchar (50) NOT NULL,
    dob         date,
    updated_at  timestamp
);

--05 Insert Customer Values
INSERT INTO customers (name, dob, updated_at) VALUES
    ('Thai Son'    , '1988-05-15', '2019-11-07 23:31:40'),
    ('Thai Binh'   , '1993-07-13', '2019-11-07 23:31:40'),
    ('Minh Anh'    , '1982-01-01', '2019-11-07 23:31:40'),
    ('Thanh Nguyen', '1985-12-04', '2019-11-07 23:31:40'),
    ('Duc Nguyen'  , '1997-10-03', '2019-11-07 23:31:40')


