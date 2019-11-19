--00 Create Databse
CREATE DATABASE customer_api;
\c customer_api;

--01 Create Table
DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
	id int PRIMARY KEY ,
	name varchar(100) not null,
	dob date not null,
	updated_at timestamp
);

--02 Insert Customer Values
INSERT INTO customers VALUES
    ('Thai Son'    , '1988-05-15', '2019-11-07 23:31:40'),
    ('Thai Binh'   , '1993-07-13', '2019-11-07 23:31:40'),
    ('Minh Anh'    , '1982-01-01', '2019-11-07 23:31:40'),
    ('Name04'      , '2011-12-01', '2019-11-07 23:31:40'),
    ('Name05'      , '2018-05-06', '2019-08-16 08:09:01')


