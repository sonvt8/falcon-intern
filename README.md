# Project Name

Introduction for running endpoint CUSTOMER

## Installation

```pipenv sync``` will install the exact versions specified in pipfile.lock

## Usage

Run file model.py, let `faker` help you to create some dummy data in your database <br>
You may get the notification:

>Connection fail. Please, modify parameters in .env to connect database

Don't worry, just find sample_env.py that is automatically created in your directory and fill all parameters included in this for your connection to database.

Let run `gunicorn` to start your WSGI server by typing the command `gunicorn Customer.app:api --reload` in Pycharm's terminal (NOTE:I am using port 8000 to work with my endpoint)
## Contributing

1.  Now, let start with POST method to creat a new customer in your list:
    * Using Postman:<br>
    Choosing POST method, then add the link in your browser: `localhost:8000/customers`. In the tab `Body`, switch the type to `raw`, then add your JSON data in body (NOTE: the id and updated_at will be created from database, you do not need add them in your JSON), e.g:
`{
   "name" :  "Thang",
   "dob"  :  "1997-11-11"
}`
    * Using httpie: `echo '{"name": "Thang", "dob": "1997-11-11"}' | http POST http://localhost:8000/customers`

2. Next, let try with GET method to read data from your database:
    * Using Postman:<br>
    Choosing GET method, then add the link in your browser: `localhost:your_port/customers` to find all the list of customers existed in your database or `localhost:your_port/customers/5` with `5` is the id of customer you want to view the profile
    * Using httpie:  `http :8000/customers`
    
3.  Playing with PUT method:
    * Using Postman:<br>
    Choosing PUT method, then add the link in your browser: `localhost:8000/customers/3` with `3` is id of customer you want to update the information. In the tab `Body`, add your JSON, e.g:
`{
   "name" :  "Phat",
   "dob"  :  "1992-12-13"
}`
    * Using httpie: `echo '{"name" : "Phat", "dob"    :  "1992-12-13" }' | http PUT http://localhost:8000/customers/3`
    
4.  Finally, DELETE method:
    * Using Postman:<br>
    Choosing DELETE method, then add the link in your browser: `localhost:8000/customers/3` with `3` is id of customer you want to delete from your database
    * Using httpie:  `http DELETE http://localhost:8000/customers/3`