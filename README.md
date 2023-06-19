# International Language School Database
This project refers to a one-tier data pipeline for SQL data ingestion and has the objective of implementing a mutable database using Python Object Oriented so that, initially use SQLite for the structure of the application and a bit further switch to a PostgreSQL and MySQL without the necessity of altering the python code, just include a new connection with your tasks, being that it will be used terraform for build an EC2 instance and docker for create containers for both databases.  

## Initial Structure: for a while, this will be the structure of the application
 - app/
    - data/
        - db_sqlite.db
    - controller/
    - interface/
    - model/
    - ingestion_sql.py
    - terraform/
    - app.py
    - docker-compose.py

## Features: 
It will be used pylint to keep code in conforming PEP8 and pre-commit to apply and update requirements.txt of the project, and still verify pylint on commit

## 1. Database
Here had been building the database classes, to be able to make a mutable database using interfaces of the Object Oriented Programming, that use the abstracts method "get_connection()" and "close_connection()" to may the connection establishment and close with the database. To provide data for the database had been used the library "Faker()" that provides random data to make ingestion into the tables: teacher, client, participant, and course. In the first place, the modeling had been doing it in SQLite and a bit further, it will make create new connections, like, PostgreSQL and MySQL.


## References: 
- https://www.freecodecamp.org/news/connect-python-with-sql/
- https://github.com/thecraigd/Python_SQL/tree/master