Python - Object Relational Mapping
Description
This project explores the use of MySQLdb and SQLAlchemy to interact with a MySQL database from Python scripts. It covers both writing raw SQL queries directly and using an ORM to map Python classes to database tables — allowing database manipulation without writing SQL.
Learning Objectives
By the end of this project, you should be able to explain:

How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python class to a MySQL table

Requirements

Ubuntu 20.04 LTS / Debian
Python 3.8+
MySQL 8.0 / MariaDB
MySQLdb module version 2.0.x
SQLAlchemy module version 1.4.x

Installation
bash# Install dependencies
sudo apt-get install python3-dev libmariadb-dev zlib1g-dev

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install mysqlclient==2.0.3
pip install SQLAlchemy==1.4.22
Tasks
#TaskDescription0Get all statesFetch all states from the database using MySQLdb1Filter statesFilter states by name using MySQLdb2Filter states by user inputFilter states based on user-provided input3SQL Injection...Prevent SQL injection with safe query methods4Cities by statesList all cities with their corresponding states5All cities by stateFetch all cities of a given state6First state modelCreate a State model using SQLAlchemy7All states via SQLAlchemyFetch all states using SQLAlchemy ORM8First stateFetch the first state using SQLAlchemy9Contains 'a'Fetch all states containing the letter a10Get a stateFetch a state by name using SQLAlchemy11Add a new stateInsert a new state using SQLAlchemy12Update a stateUpdate an existing state using SQLAlchemy13Delete statesDelete states based on a condition using SQLAlchemy14Cities in stateFetch all cities of a state using SQLAlchemy relationship
Technologies Used

Python 3 — scripting language
MySQLdb — low-level MySQL connection and raw SQL queries
SQLAlchemy — ORM for mapping Python classes to database tables
MariaDB / MySQL — relational database

Author
Tahmina Alijewa
