import datetime

from database import (
    calculate_average_salary_by_department,
    create_connection,
    create_table,
    delete_employee,
    insert_employee,
    query_all_employees_sorted_by_hire_date,
    query_employees_by_department,
    update_employee,
)


def cli_menu():
    """Display the CLI menu options."""
    print("\nEmployee Management System")
    print("1. Insert new employee record")
    print("2. Query employees by department")
    print("3. List all employees sorted by hire date")
    print("4. Update employee record")
    print("5. Delete employee record")
    print("6. Calculate average salary by department")
    print("7. Exit")


def main():
    database = "employees.db"
    conn = create_connection(database)
    create_table(conn)

    while True:
        cli_menu()
        choice = input("Select an option (1-7): ")

        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            try:
                salary = float(input("Enter salary: "))
            except ValueError:
                print("Invalid salary input. Please enter a numeric value.")
                continue
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(hire_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            try:
                insert_employee(conn, name, department, salary, hire_date)
                print("Employee record inserted successfully.")
            except Exception as e:
                print(f"Error inserting employee: {e}")

        elif choice == "2":
            department = input("Enter department to query: ")
            try:
                employees = query_employees_by_department(conn, department)
                if employees:
                    print(f"Employees in department '{department}':")
                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found in that department.")
            except Exception as e:
                print(f"Error querying employees: {e}")

        elif choice == "3":
            try:
                employees = query_all_employees_sorted_by_hire_date(conn)
                if employees:
                    print("Employees sorted by hire date:")
                    for emp in employees:
                        print(emp)
                else:
                    print("No employee records found.")
            except Exception as e:
                print(f"Error querying employees: {e}")

        elif choice == "4":
            try:
                employee_id = int(input("Enter employee ID to update: "))
            except ValueError:
                print("Invalid employee ID.")
                continue
            name = input("Enter new name: ")
            department = input("Enter new department: ")
            try:
                salary = float(input("Enter new salary: "))
            except ValueError:
                print("Invalid salary input.")
                continue
            hire_date = input("Enter new hire date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(hire_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue
            try:
                update_employee(conn, employee_id, name, department, salary, hire_date)
                print("Employee record updated successfully.")
            except Exception as e:
                print(f"Error updating employee: {e}")

        elif choice == "5":
            try:
                employee_id = int(input("Enter employee ID to delete: "))
            except ValueError:
                print("Invalid employee ID.")
                continue
            try:
                delete_employee(conn, employee_id)
                print("Employee record deleted successfully.")
            except Exception as e:
                print(f"Error deleting employee: {e}")

        elif choice == "6":
            department = input("Enter department for average salary calculation: ")
            try:
                avg_salary = calculate_average_salary_by_department(conn, department)
                print(f"Average salary in {department} department: {avg_salary:.2f}")
            except Exception as e:
                print(f"Error calculating average salary: {e}")

        elif choice == "7":
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 7.")

    conn.close()


if __name__ == "__main__":
    main()
