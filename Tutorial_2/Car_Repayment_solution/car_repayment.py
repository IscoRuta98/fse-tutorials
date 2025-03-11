import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')


def calculate_monthly_repayment(price: float, years: float, annual_interest_rate: float, deposit: float = 0.0) -> float:
    """
    Calculate the monthly repayment for a car loan.

    This function computes the monthly repayment by first determining the loan amount
    (price minus deposit) and then applying the amortizing loan formula.

    Formula:
      loan_amount = price - deposit
      monthly_interest_rate = (annual_interest_rate / 100) / 12
      number_of_payments = years * 12
      If annual_interest_rate is zero:
          monthly_repayment = loan_amount / number_of_payments
      Otherwise:
          monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-number_of_payments))

    :param price: float - the total price of the car.
    :param years: float - the number of years over which the loan will be repaid.
    :param annual_interest_rate: float - the annual interest rate as a percentage.
    :param deposit: float - an initial deposit (default is 0.0).
    :return: float - the calculated monthly repayment.
    :raises ValueError: if any input is negative or if deposit exceeds price.
    """
    logging.info(f"Calculating monthly repayment with price={price}, years={years}, "
                  f"annual_interest_rate={annual_interest_rate}, deposit={deposit}")

    if price < 0:
        raise ValueError("Price cannot be negative.")
    if years < 0:
        raise ValueError("Years cannot be negative.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if deposit < 0:
        raise ValueError("Deposit cannot be negative.")
    if deposit > price:
        raise ValueError("Deposit cannot exceed the price of the car.")

    loan_amount = price - deposit
    number_of_payments = years * 12

    if number_of_payments <= 0:
        raise ValueError("The number of payments must be greater than 0. Check the value of years.")

    if annual_interest_rate == 0:
        monthly_repayment = loan_amount / number_of_payments
    else:
        monthly_interest_rate = (annual_interest_rate / 100) / 12
        monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-number_of_payments))

    logging.info(f"Calculated monthly repayment: {monthly_repayment}")
    return monthly_repayment


def get_user_input() -> tuple[float, float, float, float]:
    """
    Prompt the user to input the car price, number of years for repayment,
    annual interest rate, and deposit.

    This function converts the inputs to float and handles conversion errors by
    logging and raising a ValueError.

    :return: tuple (price, years, annual_interest_rate, deposit)
    :raises ValueError: if the input conversion fails.
    """
    try:
        price = float(input("Enter the price of the car: "))
        years = float(input("Enter the number of years to repay the loan: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        deposit_input = input("Enter the deposit amount (press Enter for 0): ")
        deposit = float(deposit_input) if deposit_input.strip() != "" else 0.0
    except ValueError as e:
        logging.error("Invalid input. Please enter numeric values.")
        raise ValueError("Invalid input. Please ensure all inputs are numbers.") from e

    logging.debug(f"User input received: price={price}, years={years}, "
                  f"annual_interest_rate={annual_interest_rate}, deposit={deposit}")
    return price, years, annual_interest_rate, deposit


def main():
    """
    Main entry point of the program.

    This function retrieves user input, calculates the monthly repayment, and displays the result.
    It handles exceptions gracefully and logs errors when they occur.
    """
    try:
        price, years, annual_interest_rate, deposit = get_user_input()

        repayment = calculate_monthly_repayment(price, years, annual_interest_rate, deposit)
        print(f"Your monthly repayment is: ${repayment:.2f}")
    except ValueError as e:
        logging.error(f"Error in calculation: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
