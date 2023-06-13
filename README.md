# International Language School Database
This project refers to a one-tier data pipeline for SQL data ingestion and has the objective of implementing a mutable database using Python Object Oriented so that, initially use SQLite for the structure of the application and a bit further switch to a PostgreSQL and MySQL without the necessity of altering the python code, just include a new connection with your tasks, being that it will be used terraform for build an EC2 instance and docker for create containers for both databases.  

## Initial Structure: for a while, this will be the structure of the application
 - app/
    - database/
        - controller/
        - interface/
        - model/
        - main.py
        - sqlite.db
    - terraform/
    - app.py
    - docker-compose.py

## Features: 
- It will be used pylint to keep code in conforming PEP8 and pytest to make code verifications

## 1. Database


## References: 
- https://www.freecodecamp.org/news/connect-python-with-sql/
- https://github.com/thecraigd/Python_SQL/tree/master