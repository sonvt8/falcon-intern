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
    (1,'Ronaldo', '19990805', '2019-01-12 07:00:01'),
    (2,'Modric',  '19890715', '2019-10-01 00:00:01');
--     (3,'Ramos',   '20091205', '2019-11-01 08:00:01'),
--     (4,'Hazard',  '19690125', '2019-11-24 11:20:01');


