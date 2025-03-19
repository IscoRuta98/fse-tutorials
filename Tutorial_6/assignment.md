# Practical Assignment: FastAPI TODO/Task List Server

## Objective
The aim of this practical is to create your own web server using FastAPI and SQLite. The web server will allow users to track their TODO/Task list.

## TODO Task Properties
Each TODO item should have the following properties:

- **Id**: String
- **Task Title**: String
- **Completed**: Boolean

## Requirements
Create a FastAPI application connected to a local SQLite3 database (see [hero](/Tutorial_6/hero/)) example to draw inspiration from.

### Endpoints
You must implement the following endpoints:

- `GET` all Tasks
- `GET` Tasks based on particular field(s)
- `POST` (create) a new Task
- `PUT` (update) an existing Task
- `DELETE` an existing Task

### Endpoint Expectations
For each endpoint, include:
- Data validation
- HTTP Exceptions
- Appropriate HTTP Status Codes

---

### Submission
In a GitHub repository, Submit your FastAPI project including all Python files (e.g. `db.py`, `main.py`, `models.py`) along with a working `database.db` SQLite file demonstrating your API functionality.

