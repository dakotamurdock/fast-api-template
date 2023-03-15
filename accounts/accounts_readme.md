# Accounts Read-Me

To start, 'accounts' is created as a Python package so that it can be imported. 

The accounts package manages all functions and database interactions for endpoints that begin with '/accounts'

The following files exist in the 'accounts' package:
 - models.py
 - router.py
 - schema.py
 - services.py
 - validator.py
 
## What are these files?
### models.py

To start, models.py is where Python classes are specified that relate to database tables. All the classes in this
file should inherit the SQLAlchemy Base class. This is so SQLAlchemy can handle mapping the Python objects to the 
database tables. 

The classes from this file are instantiated in the services.py file and the validator.py file (i.e. the files that 
define functions to interact with the database).

### router.py

Next, router.py exists to create API endpoints. Router is where the application looks at the endpoint and determines 
what it needs to do. Depending on the endpoint it will call the appropriate function. These functions are contained in
services.py.

The router functions defined in this file are used in the overall main.py file.

### services.py

This is where you define functions to actually do things. The router.py file calls the functions contained in this 
services.py file which interacts with the classes in models.py. In most cases there should be a function contained in
services.py that corresponds with a REST API method (post, get, put, delete).

The functions in this file are used in the router.py file.

### schema.py

This file utilizes Pydantic to specify the response model. 

So let's say a 'GET' method was called. The router file 
appropriately handles that request and calls the corresponding function in the services.py file. SQLAlchemy handles the 
SQL required to get the appropriate data from the database corresponding to the request, but then we have to return that 
data to the client. This schema file, using Pydantic, specifies how to return that data. 

For a 'POST' method, this file uses Pydantic as a type validator. It makes sure the data passed by the client is of the 
appropriate type. If you've specified a Pydantic schema with, let's say for example, a birthdate that should be of type 
datetime, but the client passed a value that was a String, using Pydantic, this error is caught here.

The schema classes specified in this file are used in the router.py file.

### validator.py

This file is used to check the database for things before executing a function in services.py. This could be confirming
that a record exists, or it could be the opposite -- making sure a record doesn't exist. An example would be checking to
see if an email has already been used, and if it has, don't create a new record with that email. This file is using 
SQLAlchemy to interact with the database. 

Functions created in this file are used in the router.py file.