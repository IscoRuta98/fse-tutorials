# Assignment: Annual Investment Calculator

## Objective

In this assignment, you will build a Python program that calculates the potential growth of an annual investment strategy. The user will be prompted for:

- **Monthly Investment Amount** (in Rands)
- **Expected Annual Return** (as a percentage)
- **Period** (in years)

Your program should then calculate and display:

1. **Investment Amount (Rands)** – The total amount the user invests over the entire period.
2. **Expected Amount (Rands)** – The total value of the investment at the end of the period, given the expected annual return.
3. **Wealth Gain (Rands)** – The difference between the Expected Amount and the total Investment Amount.

You are expected to:
- Validate user inputs and handle errors appropriately.
- Follow Python style guides (PEP 8 and Google Python Style).
- Use logging to provide debug-level information.
- Write unit tests using **pytest** to ensure your code works as expected.

---

## Part 1: Module Implementation

### Requirements

1. **Create a module named `annual_investment_calculator.py`** containing at least the following:

   - **`calculate_investment_growth(monthly_investment: float, annual_return: float, years: float) -> tuple[float, float, float]`**

     - **Purpose:**  
       Calculate the final investment value based on monthly contributions, an annual return rate, and a given number of years.

     - **Implementation Detail:**  
       - ![Implementation of the Formulae](/Tutorial_2/formulae.png)

       - **Validate** that `monthly_investment`, `annual_return`, and `years` are non-negative. Raise a `ValueError` with a descriptive message if validation fails.
       - **Return** a tuple of `(investment_amount, expected_amount, wealth_gain)`.

     - **Logging:**  
       - Log the input values and the resulting calculations at the debug level.

     - **Docstring:**  
       Provide a clear docstring describing the function’s parameters, return value, and any exceptions raised.

   - **`get_user_input() -> tuple[float, float, float]`**

     - **Purpose:**  
       Prompt the user to enter the monthly investment amount, annual return percentage, and the investment period in years.

     - **Implementation Detail:**  
       - Convert each input to `float`.
       - Catch any conversion errors, log an appropriate message, and raise a `ValueError`.
       - Return a tuple `(monthly_investment, annual_return, years)`.

   - **`main()`**

     - **Purpose:**  
       Serve as the entry point for running the program.

     - **Implementation Detail:**  
       - Call `get_user_input()` to retrieve user data.
       - Pass the inputs to `calculate_investment_growth(...)`.
       - Print the **Investment Amount**, **Expected Amount**, and **Wealth Gain** in a user-friendly format.
       - Use a try/except block to handle any `ValueError` exceptions raised by input validation or calculation.

2. **Code Quality:**
   - Follow [PEP 8](https://peps.python.org/pep-0008/) and the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
   - Use descriptive variable names, type hints, and docstrings for functions (PEP-257).
   - Configure and use the `logging` module for debug-level logs.

---

## Part 2: Exception Handling

1. **Validation and Error Handling:**
   - Validate that all numeric inputs are non-negative.
   - If any validation fails, raise a `ValueError` with an informative error message.
   - Log error messages using the `logging` module.

2. **Demonstration of Behavior:**
   - Show in your code (through logs or printed messages) how the program behaves when invalid inputs are provided.

---

## Part 3: Unit Testing with pytest

1. **Test Suite Setup:**
   - Create a separate file named `test_annual_investment_calculator.py`.
   - Write **pytest** tests for each function in `annual_investment_calculator.py`.

2. **Test Coverage:**
   - **Valid Cases:**  
     Check that valid inputs produce the expected results. Use `pytest.approx` to handle floating-point comparisons.
   - **Error Cases:**  
     Use `pytest.raises(ValueError)` to confirm that invalid inputs (e.g., negative values for monthly investment or years) raise a `ValueError`.
   - **Edge Cases:**  
     - A zero annual return.
     - A zero monthly investment amount.
     - A zero investment period (years).

---

## Part 4: Submission

1. **Deliverables:**
   - `annual_investment_calculator.py`
   - `test_annual_investment_calculator.py`

2. **Submission Guidelines:**
   - Ensure your code is well-documented, passes all tests, and meets style guide requirements.
   - Provide any instructions needed to run your program and tests (e.g., `python annual_investment_calculator.py` and `pytest`).

---

## Hints and Resources

- **Python Style Guides:**
  - [PEP 8](https://peps.python.org/pep-0008/)
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

- **Logging:**
  - Import and configure the `logging` module to log important events at `logging.DEBUG` level or above.
  - Example:
    ```python
    import logging
    logging.basicConfig(level=logging.DEBUG)
    ```

- **pytest:**
  - [pytest Documentation](https://docs.pytest.org/en/latest/)
  - Use `assert` statements for validations:
    ```python
    import pytest

    def test_something():
        assert 1 == 1
    ```
  - Use `pytest.approx` for floating-point comparisons and `pytest.raises` for testing exceptions.

- **Mathematical Formulas:**
  - [Future Value of an Annuity](https://en.wikipedia.org/wiki/Annuity_(finance_theory)#Future_value_of_an_annuity)

By completing this assignment, you will learn how to structure a small Python project, handle user inputs safely, calculate financial projections, log debug information, and thoroughly test your code using pytest.
