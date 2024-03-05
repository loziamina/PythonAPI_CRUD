## TODO list API

- This is a REST API built using the FastAPI library to manage a list of to-do tasks stored in sqlite database.

## Features
 - Create, read , update, and delete to-do tasks.

## Endpoints

- functionality method path
    - create a todo item POST /todo
    - read a todo list item GET /todo/{id}
    - update a todo item PUT /todo/{id}
    - delete a todo item DELETE /todo/{id}
    - read all todo items GET /todo

## Requirements
- Python 3.11+
- Fast-API
- sqlite/sqlalchemy
- pydantic
- uvicorn

## Installation
Run the command below to install necessary modules.
poetry add fastapi / uvicorn uvicorn[standard]
Database Structure
+---------+-----------------+
|      id | task            | 
+---------+-----------------+
|         |                 |     
+---------+-----------------+


## Usage

- Run :  uvicorn main:app --reload command.
Now it will be running in localhost at port 8000.
Checkout at http://127.0.0.1:8000/docs