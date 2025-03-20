import logging
import sqlite3

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a connection to the SQLite database specified by db_file."""
    try:
        conn = sqlite3.connect(db_file)
        logging.debug(f"Connected to database: {db_file}")
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        raise


def create_table(conn: sqlite3.Connection):
    """Create the employees table if it doesn't already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL,
                hire_date TEXT NOT NULL
            );
        """
        )
        conn.commit()
        logging.debug("Employees table created or already exists.")
    except sqlite3.Error as e:
        logging.error(f"Error creating table: {e}")
        raise


def insert_employee(
    conn: sqlite3.Connection, name: str, department: str, salary: float, hire_date: str
):
    """Insert a new employee record into the employees table."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO employees (name, department, salary, hire_date)
            VALUES (?, ?, ?, ?);
        """,
            (name, department, salary, hire_date),
        )
        conn.commit()
        logging.debug(f"Inserted employee: {name}, {department}, {salary}, {hire_date}")
    except sqlite3.Error as e:
        logging.error(f"Error inserting employee: {e}")
        raise


def query_employees_by_department(conn: sqlite3.Connection, department: str):
    """Query and return employee records by department."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM employees WHERE department = ?;
        """,
            (department,),
        )
        results = cursor.fetchall()
        logging.debug(f"Queried employees in department '{department}': {results}")
        return results
    except sqlite3.Error as e:
        logging.error(f"Error querying employees: {e}")
        raise


def query_all_employees_sorted_by_hire_date(conn: sqlite3.Connection):
    """Return all employee records sorted by hire_date."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM employees ORDER BY hire_date ASC;
        """
        )
        results = cursor.fetchall()
        logging.debug("Queried all employees sorted by hire_date.")
        return results
    except sqlite3.Error as e:
        logging.error(f"Error querying employees: {e}")
        raise


def update_employee(
    conn: sqlite3.Connection,
    employee_id: int,
    name: str,
    department: str,
    salary: float,
    hire_date: str,
):
    """Update an employee's details."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE employees
            SET name = ?, department = ?, salary = ?, hire_date = ?
            WHERE employee_id = ?;
        """,
            (name, department, salary, hire_date, employee_id),
        )
        conn.commit()
        logging.debug(f"Updated employee with ID {employee_id}.")
    except sqlite3.Error as e:
        logging.error(f"Error updating employee: {e}")
        raise


def delete_employee(conn: sqlite3.Connection, employee_id: int):
    """Delete an employee record by employee_id."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM employees WHERE employee_id = ?;
        """,
            (employee_id,),
        )
        conn.commit()
        logging.debug(f"Deleted employee with ID {employee_id}.")
    except sqlite3.Error as e:
        logging.error(f"Error deleting employee: {e}")
        raise


def calculate_average_salary_by_department(
    conn: sqlite3.Connection, department: str
) -> float:
    """Calculate and return the average salary for a given department."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT AVG(salary) FROM employees WHERE department = ?;
        """,
            (department,),
        )
        result = cursor.fetchone()[0]
        avg_salary = result if result is not None else 0.0
        logging.debug(f"Average salary in department '{department}': {avg_salary}")
        return avg_salary
    except sqlite3.Error as e:
        logging.error(f"Error calculating average salary: {e}")
        raise
