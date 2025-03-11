import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def calculate_investment_growth(
    monthly_investment: float, annual_return: float, years: float
) -> tuple[float, float, float]:
    """
    Calculate the growth of an investment based on monthly contributions and an expected annual return.

    This function computes:
      - Investment Amount: Total amount contributed over the entire period.
      - Expected Amount: Future value of the investment using the future value of an annuity formula
        (with monthly compounding). If the annual return is 0, the Expected Amount equals the Investment Amount.
      - Wealth Gain: The difference between the Expected Amount and the Investment Amount.

    Formula details:
      - num_months = years * 12
      - Investment Amount = monthly_investment * num_months
      - If annual_return is not 0:
          monthly_rate = (annual_return / 100) / 12
          Expected Amount = monthly_investment * ((1 + monthly_rate)**num_months - 1) / monthly_rate
        Otherwise:
          Expected Amount = Investment Amount
      - Wealth Gain = Expected Amount - Investment Amount

    :param monthly_investment: The monthly amount invested (in Rands).
    :param annual_return: The expected annual return as a percentage.
    :param years: The investment period in years.
    :return: A tuple (investment_amount, expected_amount, wealth_gain).
    :raises ValueError: If any of the input values are negative.
    """
    logging.debug(
        f"Calculating investment growth with monthly_investment={monthly_investment}, annual_return={annual_return}, years={years}"
    )

    if monthly_investment < 0:
        raise ValueError("Monthly investment must be non-negative.")
    if annual_return < 0:
        raise ValueError("Annual return must be non-negative.")
    if years < 0:
        raise ValueError("Investment period (years) must be non-negative.")

    num_months = years * 12
    investment_amount = monthly_investment * num_months
    logging.debug(
        f"Number of months: {num_months}, Investment Amount: {investment_amount}"
    )

    if annual_return == 0:
        expected_amount = investment_amount
    else:
        monthly_rate = (annual_return / 100) / 12
        expected_amount = (
            monthly_investment * ((1 + monthly_rate) ** num_months - 1) / monthly_rate
        )

    wealth_gain = expected_amount - investment_amount
    logging.debug(f"Expected Amount: {expected_amount}, Wealth Gain: {wealth_gain}")

    return investment_amount, expected_amount, wealth_gain


def get_user_input() -> tuple[float, float, float]:
    """
    Prompt the user to enter the monthly investment amount, expected annual return, and the investment period in years.

    :return: A tuple (monthly_investment, annual_return, years).
    :raises ValueError: If the input conversion fails.
    """
    try:
        monthly_investment = float(
            input("Enter the monthly investment amount (in Rands): ")
        )
        annual_return = float(input("Enter the expected annual return (in %): "))
        years = float(input("Enter the investment period (in years): "))
    except ValueError as e:
        logging.error("Invalid input. Please enter numeric values.")
        raise ValueError("Invalid input. Please ensure all inputs are numbers.") from e

    logging.debug(
        f"User input received: monthly_investment={monthly_investment}, annual_return={annual_return}, years={years}"
    )
    return monthly_investment, annual_return, years


def main():
    """
    Main entry point for the Annual Investment Calculator.

    Retrieves user input, calculates the investment growth, and displays the results.
    Handles any exceptions from input validation or calculation.
    """
    try:
        monthly_investment, annual_return, years = get_user_input()
        investment_amount, expected_amount, wealth_gain = calculate_investment_growth(
            monthly_investment, annual_return, years
        )

        print(f"Investment Amount (Rands): {investment_amount:.2f}")
        print(f"Expected Amount (Rands): {expected_amount:.2f}")
        print(f"Wealth Gain (Rands): {wealth_gain:.2f}")
    except ValueError as e:
        logging.error(f"Error in calculation: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
