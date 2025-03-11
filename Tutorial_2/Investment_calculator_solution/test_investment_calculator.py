import pytest
from investment_calculator import calculate_investment_growth, get_user_input


def test_calculate_investment_growth_normal():
    """
    Test normal calculation with a non-zero annual return.
    Example: monthly_investment=1000, annual_return=12, years=10.
    """
    monthly_investment = 1000
    annual_return = 12  # 12% annual return
    years = 10
    num_months = years * 12
    expected_investment = monthly_investment * num_months

    # Calculate monthly_rate and expected amount using the annuity formula:
    monthly_rate = (annual_return / 100) / 12
    expected_amount = (
        monthly_investment * ((1 + monthly_rate) ** num_months - 1) / monthly_rate
    )
    expected_wealth_gain = expected_amount - expected_investment

    inv_amt, exp_amt, wealth_gain = calculate_investment_growth(
        monthly_investment, annual_return, years
    )
    assert inv_amt == pytest.approx(expected_investment, rel=1e-2)
    assert exp_amt == pytest.approx(expected_amount, rel=1e-2)
    assert wealth_gain == pytest.approx(expected_wealth_gain, rel=1e-2)


def test_calculate_investment_growth_zero_return():
    """
    Test calculation when the annual return is zero.
    In this case, the expected amount should equal the investment amount.
    """
    monthly_investment = 500
    annual_return = 0
    years = 5
    num_months = years * 12
    expected_investment = monthly_investment * num_months

    inv_amt, exp_amt, wealth_gain = calculate_investment_growth(
        monthly_investment, annual_return, years
    )
    assert inv_amt == pytest.approx(expected_investment, rel=1e-2)
    assert exp_amt == pytest.approx(expected_investment, rel=1e-2)
    assert wealth_gain == pytest.approx(0, rel=1e-2)


def test_calculate_investment_growth_invalid_input():
    """
    Test that negative inputs raise a ValueError.
    """
    with pytest.raises(ValueError):
        calculate_investment_growth(-1000, 10, 5)
    with pytest.raises(ValueError):
        calculate_investment_growth(1000, -10, 5)
    with pytest.raises(ValueError):
        calculate_investment_growth(1000, 10, -5)


def test_get_user_input_valid(monkeypatch):
    """
    Test get_user_input with valid numeric inputs using monkeypatch.
    """
    inputs = iter(["1500", "8", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    monthly_investment, annual_return, years = get_user_input()
    assert monthly_investment == pytest.approx(1500.0)
    assert annual_return == pytest.approx(8.0)
    assert years == pytest.approx(7.0)


def test_get_user_input_invalid(monkeypatch):
    """
    Test get_user_input with an invalid (non-numeric) input.
    """
    inputs = iter(["abc", "8", "7"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    with pytest.raises(ValueError):
        get_user_input()
