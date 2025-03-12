# Databases and SQL

The aim of this tutorial is to get you confortable with creating SQL tables using Python's built-in `sqlite3` module and perform CRUD operations.

# Using `sqlite3` in Python for building a Student Records Management System

This guide will walk you through the process of using Python’s built-in `sqlite3` module to create and manage a simple Student Records Management System. We will cover how to create a database, build a table, and perform basic CRUD (Create, Read, Update, Delete) operations.

*Reference: [Work With SQLite in Python Handbook](https://www.freecodecamp.org/news/work-with-sqlite-in-python-handbook/)*


## Connecting to a SQLite database

1. Import `sqlite3` and connect to the database.
```python
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_database.db')
```

2. Create a Cursor 

Next step is to create a cursor object. The cursor is responsible for executing SQL commands and queries on the database.

```python
# Create a cursor object
cursor = connection.cursor()
```

3. Close the connection

After you’ve finished working with the database, it’s important to close the connection to free up any resources, by using the following command:

```python
# Close the database connection
connection.close()
```
You should only close the connection once you’re done with all your operations.

When you run your Python script, a file named my_database.db will be created in your current working directory. You’ve now successfully created your first SQLite database!

However, there is a more efficient way of connecting to SQLite Database....

```python
import sqlite3

# Step 1: Use 'with' to connect to the database (or create one) and automatically close it when done
with sqlite3.connect('my_database.db') as connection:

    # Step 2: Create a cursor object to interact with the database
    cursor = connection.cursor()

    print("Database created and connected successfully!")

# No need to call connection.close(); it's done automatically. 
```

## How to Create Database Tables

The SQL command to create this table would look like this:
```sql
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
```
We can execute this `CREATE TABLE` SQL command in Python using the `sqlite3` library...

```python
import sqlite3

# Use 'with' to connect to the SQLite database as it automatically close the connection when done
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''

    # Execute the SQL command
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Table 'Students' created successfully!")
```
 * Side Note: In simple terms, context managers (such as `with` statement) help you manage resources (like files, network connections, etc.) by ensuring that the setup and cleanup code runs automatically, making your code cleaner, safer, and easier to maintain.

For more details, checkout the PythonTips book on [context managers](https://book.pythontips.com/en/latest/context_managers.html).

## Data Types in SQLite and Their Mapping to Python

Below is quick overview of common SQLite data types and how they map to Python types:
![SQLite Data types and their mapping to Python](/Tutorial_3/data_types_mapping.png)

## Inserting Single Record

The basic SQL syntax for inserting a single record:

```sql
INSERT INTO Students (name, age, email) 
VALUES ('John Doe', 20, 'johndoe@example.com');
```

Instead of writing SQL directly in our Python script with hardcoded values, we’ll use parameterized queries to make our code more secure and flexible. Parameterized queries help prevent SQL injection, a common attack where malicious users can manipulate the SQL query by passing harmful input.

Here’s how we can insert a single record into the Students table using a parameterized query:

```python
import sqlite3

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    student_data = ('Jane Doe', 23, 'jane@example.com')

    cursor.execute(insert_query, student_data)

    # Commit the changes automatically
    connection.commit()

    # No need to call connection.close(); it's done automatically!
    print("Record inserted successfully!")
```

The `?` placeholders represent the values to be inserted into the table. 
The actual values are passed as a tuple (student_data) in the cursor.execute() method.

## Handling SQL Injection

SQL injection is a security vulnerability where attackers can insert or manipulate SQL queries by providing harmful input. For example, an attacker might try to inject code like `'; DROP TABLE Students; --` to delete the table.

By using parameterized queries (as shown above), we avoid this issue. The `?` placeholders in parameterized queries ensure that input values are treated as data, not as part of the SQL command. This makes it impossible for malicious code to be executed.

## Insert Multiple Records

You can use the executemany() method in Python to insert several records. 
This method takes a list of tuples, where each tuple represents one record. We will make use of the `Faker` library ot simulate fake data.

```python
from faker import Faker
import sqlite3

# Initialize Faker
fake = Faker(['en_IN'])

# Use 'with' to open and close the connection automatically
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # Insert a record into the Students table
    insert_query = '''
    INSERT INTO Students (name, age, email) 
    VALUES (?, ?, ?);
    '''
    students_data = [(fake.name(), fake.random_int(
        min=18, max=25), fake.email()) for _ in range(5)]

    # Execute the query for multiple records
    cursor.executemany(insert_query, students_data)

    # Commit the changes
    connection.commit()

    # Print confirmation message
    print("Fake student records inserted successfully!")
```

## How to Query Data

There's different methods for fetching data in `sqlite3` module, including: `fetchone()`, `fetchall()`, and `fetchmany()`.
See the following python scripts:

## Updating Existing Records

if we want to update a student's age, the SQL command would look like this:

```sql
UPDATE Students 
SET age = 21 
WHERE name = 'Jane Doe';
```

Python code to update a specific student's age in the Students table.

```python
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # SQL command to update a student's age
    update_query = '''
    UPDATE Students 
    SET age = ? 
    WHERE name = ?;
    '''

    # Data for the update
    new_age = 21
    student_name = 'Jane Doe'

    # Execute the SQL command with the data
    cursor.execute(update_query, (new_age, student_name))

    # Commit the changes to save the update
    connection.commit()

    # Print a confirmation message
    print(f"Updated age for {student_name} to {new_age}.")
```

## Delete Records from the Table

To delete a student named 'Jane Doe', the SQL command would look like this:

```sql
DELETE FROM Students 
WHERE name = 'Jane Doe';
```

Python code to delete a specific student from our Students table using the `with` statement.

```python
import sqlite3

# Use 'with' to connect to the SQLite database
with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    # SQL command to delete a student
    delete_query = '''
    DELETE FROM Students 
    WHERE name = ?;
    '''

    # Name of the student to be deleted
    student_name = 'Jane Doe'

    # Execute the SQL command with the data
    cursor.execute(delete_query, (student_name,))

    # Commit the changes to save the deletion
    connection.commit()

    # Print a confirmation message
    print(f"Deleted student record for {student_name}.")
```

**Sidenote**:
- Always use the `WHERE` clause when updating or deleting records to avoid modifying or removing all rows in the table. Without a `WHERE` clause, the command affects every row in the table.

## Exporting Data from SQLite to CSV

Exporting data to a CSV (Comma-Separated Values) file is possible with Python’s built-in libraries.

```python
import sqlite3
import csv

def export_to_csv(file_name):
    """Export data from the Customers table to a CSV file."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Execute a query to fetch all customer data
        cursor.execute("SELECT * FROM Students;")
        customers = cursor.fetchall()

        # Write data to CSV
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['ID', 'Name', 'Age', 'Email'])  # Writing header
            csv_writer.writerows(customers)  # Writing data rows

        print(f"Data exported successfully to {file_name}.")

# Example usage
export_to_csv('students.csv')
```

## Importing Data to SQLite form CSV
Importing data from a CSV (Comma-Separated Values) file is also possible with Python’s built-in libraries.

```python
import csv
import sqlite3


def import_from_csv(file_name):
    """Import data from a CSV file into the Students table."""
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Open the CSV file for reading
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row

            # Insert each row into the Students table
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO Students (name, age, email) VALUES (?, ?, ?);", (row[0], row[1], row[2]))

        connection.commit()
        print(f"Data imported successfully from {file_name}.")


# Example usage
import_from_csv('student_data.csv')
```

# Assignment

Attempt the [Employment Management System problem](/Tutorial_3/employment_management_system.md)