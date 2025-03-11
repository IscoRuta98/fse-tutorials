# Employee Management System

## Objective

Develop a Python application that manages employee data using Python's `sqlite3` module. 

## Tasks

### Database Design

- **Create an SQLite database** with an `employees` table containing the following fields:
  - `employee_id`: Primary Key (auto-incremented)
  - `name`: Text
  - `department`: Text
  - `salary`: Numeric (Real or Integer)
  - `hire_date`: Date (or Text in a date format)

### Implement CRUD Operations

- **Create:**  
  - Add new employee records to the database.

- **Read:**  
  - Retrieve employee records by department.
  - List all employees sorted by hire date.

- **Update:**  
  - Change details such as an employee's salary or department.

- **Delete:**  
  - Remove an employee record from the database.

### Python Code

- **Use the `sqlite3` module** to interact with the database.
- **Write modular functions** for each CRUD operation:
  - A function to **insert** new employee records.
  - A function to **query** employee data.
  - A function to **update** employee data.
  - A function to **delete** employee records.
- **Use parameterized queries** to prevent SQL injection.
- **Include error handling and logging** to track operations and manage errors effectively.

### Advanced Features

- **Command-Line Interface (CLI):**  
  - Build a Python CLI that allows managers to run queries and update employee information.
  - Add a feature that calculates the average salary per department.
  - The CLI should allow the user to do the following...

  ```
    1. Insert new employee record
    2. Query employees by department"
    3. List all employees sorted by hire date"
    4. Update employee record"
    5. Delete employee record"
    6. Calculate average salary by department"
    7. Exit"
  ```
 - Make sure your `employees` table is populated with records.


## Hints and Resources

- **Resources form Tutorial 2:**
    - [Tutorial 2](/Tutorial_2/)

- **SQLite Documentation:**  
  - [SQLite Documentation](https://www.sqlite.org/docs.html)
  
- **Python sqlite3 Module Documentation:**  
  - [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
  
- **Parameterizing Queries:**  
  - Always use parameterized queries (using placeholders like `?`) to avoid SQL injection attacks.
  
- **Logging:**  
  - Utilize Python’s `logging` module to log important operations and error messages.
  
- **Error Handling:**  
  - Implement robust error handling using try/except blocks to manage database connection issues and SQL errors.

---
