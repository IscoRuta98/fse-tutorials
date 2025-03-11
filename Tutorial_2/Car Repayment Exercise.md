# Assignment: Car Loan Repayment Calculator

## Objective

In this assignment you will build a Python program that calculates the monthly repayment for purchasing a car. Your program will prompt the user for:

- **Price of the car**
- **Number of years to pay back the price**
- **Annual interest rate** (as a percentage)
- **Deposit** (if any; optional, defaulting to zero)

The aim of this assignment is to:
- Apply input validation and robust error handling
- Use logging for debugging and tracing execution flow
- Follow Python style guides (PEP 8 & Google Python Style)
- Write comprehensive unit tests using the **pytest** framework

## Part 1: Module Implementation

### Requirements

1. **Create a module named `car_loan.py`** with at least the following functions:

   - **`calculate_monthly_repayment(price: float, years: float, annual_interest_rate: float, deposit: float = 0.0) -> float`**
     
     - **Purpose:** Calculate the monthly repayment for a car loan.
     - **Formula:**  
       Calculate the loan amount as:  
       ```
       loan_amount = price - deposit
       ```
       Then compute the monthly repayment using the formula for an amortizing loan:
       ```
       monthly_interest_rate = (annual_interest_rate / 100) / 12
       number_of_payments = years * 12
       monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-number_of_payments))
       ```
       *Note:* If the interest rate is 0%, the monthly repayment is simply the loan amount divided by the number of payments.
     
     - **Requirements:**
       - Validate that `price`, `years`, and `annual_interest_rate` are non-negative numbers.
       - Validate that `deposit` is non-negative and does not exceed the `price`.
       - If any validation fails, raise a `ValueError` with an appropriate message.
       - Log input values and the computed monthly repayment using Python’s `logging` module.
       - Include type hints and a detailed docstring.

   - **`get_user_input() -> tuple[float, float, float, float]`**
     
     - **Purpose:** Prompt the user to enter the car price, number of years to repay, annual interest rate, and deposit.
     - **Requirements:**
       - Ensure the inputs are converted to `float`.
       - Handle cases where the user inputs invalid data by catching exceptions and displaying a user-friendly error message.
       - Log errors if the conversion fails.
       - Return a tuple with the values `(price, years, annual_interest_rate, deposit)`.

   - **`main()`**
     
     - **Purpose:** The main entry point for your program.
     - **Requirements:**
       - Call `get_user_input()` to receive input.
       - Call `calculate_monthly_repayment()` with the user-provided values.
       - Display the computed monthly repayment.
       - Use a try/except block to handle any exceptions from input validation or calculation.

2. **Code Quality:**
   - Adhere to [PEP 8](https://peps.python.org/pep-0008/) and the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
   - Use descriptive variable names, clear inline comments, and proper type hints.
   - Add docstrings for each function following the PEP-257 standard.

## Part 2: Exception Handling

1. **Exception Handling:**
   - Ensure that all functions perform input validation.
   - Use try/except blocks to catch errors (e.g., `ValueError`) and log a user-friendly message.
   - Demonstrate how the program behaves when invalid input is provided.

## Part 3: Unit Testing

1. **Create a Test Suite:**
   - Create a separate file named `test_car_loan.py` using the **pytest** framework.
   - Write tests for each function in `car_loan.py`:
     - **Valid Cases:** Verify that correct inputs produce expected monthly repayments.
     - **Error Cases:** Use `pytest.raises` to check that invalid inputs (e.g., negative values or a deposit greater than the price) raise a `ValueError`.

2. **Coverage:**
   - Write tests to cover edge cases such as:
     - A zero interest rate.
     - A deposit equal to the car price.
     - Non-numeric input for user inputs (use pytest’s `monkeypatch` fixture).

## Part 4: Submission and Extra Credit

1. **Submission:**
   - Submit your `car_loan.py` and `test_car_loan.py` files.
   - Ensure your code is well-documented, follows the style guides, and passes all unit tests.

2. **Extra Credit (Optional):**
   - Extend the program by adding a function to compute the total interest paid over the life of the loan.
   - Write additional tests to cover this new function.
   - Implement integration tests to simulate a full car loan calculation scenario with various inputs.

## Hints and Resources

- **Style Guides:**
  - [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

- **Exception Handling:**
  - Use `try/except` to catch and handle exceptions.
  - Raise exceptions using `raise ValueError("Your message here")`.

- **Logging:**
  - Configure the `logging` module to output debug information:
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```
  - Log key events and error messages for traceability.

- **Unit Testing with pytest:**
  - Review the [pytest documentation](https://docs.pytest.org/en/latest/) for guidance.
  - Use assertions like `assert` and `pytest.approx` for comparing floating-point values.
  - Utilize the `monkeypatch` fixture to simulate user input.
