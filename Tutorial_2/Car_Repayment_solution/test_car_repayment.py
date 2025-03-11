import pytest
from car_repayment import calculate_monthly_repayment, get_user_input

def test_calculate_monthly_repayment_normal():
    """
    Test monthly repayment calculation with a normal non-zero interest rate.
    For a car priced at $30,000 with a $5,000 deposit, a 5-year term,
    and an annual interest rate of 5%, the monthly repayment is expected to be approximately $471.90.
    """
    price = 30000.0
    years = 5.0
    annual_interest_rate = 5.0
    deposit = 5000.0
    result = calculate_monthly_repayment(price, years, annual_interest_rate, deposit)
    # Using pytest.approx to compare floating-point numbers
    assert result == pytest.approx(471.90, rel=1e-2)

def test_calculate_monthly_repayment_zero_interest():
    """
    Test monthly repayment calculation with zero interest rate.
    The monthly repayment should equal the loan amount divided by the total number of payments.
    """
    price = 20000.0
    years = 4.0
    annual_interest_rate = 0.0
    deposit = 2000.0
    result = calculate_monthly_repayment(price, years, annual_interest_rate, deposit)
    expected = (price - deposit) / (years * 12)
    assert result == pytest.approx(expected, rel=1e-2)

def test_calculate_monthly_repayment_invalid_input():
    """
    Test that invalid inputs (negative values or deposit greater than price)
    raise a ValueError.
    """
    with pytest.raises(ValueError):
        calculate_monthly_repayment(-10000, 5, 5, 0)
    with pytest.raises(ValueError):
        calculate_monthly_repayment(15000, 5, 5, 20000)
    with pytest.raises(ValueError):
        calculate_monthly_repayment(20000, -3, 5, 0)

def test_get_user_input_valid(monkeypatch):
    """
    Test get_user_input with valid numeric inputs.
    """
    inputs = iter(['25000', '3', '4.5', '2000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_user_input()
    expected = (25000.0, 3.0, 4.5, 2000.0)
    assert result == expected

def test_get_user_input_invalid(monkeypatch):
    """
    Test get_user_input when an invalid (non-numeric) input is provided.
    """
    inputs = iter(['abc', '3', '4.5', '2000'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(ValueError):
        get_user_input()
