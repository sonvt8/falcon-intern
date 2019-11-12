--01 Create Table
DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
	id int PRIMARY KEY ,
	name varchar(100) not null,
	dob date not null,
	updated_at timestamp
);
​
--02 Insert Customer Values
INSERT INTO customers VALUES
    (1,'Ronaldo', '19990805', '2019-01-12 07:00:01'),
    (2,'Modric',  '19890715', '2019-10-01 00:00:01'),
    (3,'Ramos',   '20091205', '2019-11-01 08:00:01');

--           /Users/tommy/Documents/gigacover/falcon-intern/customers.sql
-- docker cp /Users/tommy/Documents/gigacover/falcon-intern/customers.sql sonvt8_falcon_intern_postgres:/
-- docker exec sonvt8_falcon_intern_postgres bash -c "psql -Upostgres -d customer_api -f /customers.sql"
