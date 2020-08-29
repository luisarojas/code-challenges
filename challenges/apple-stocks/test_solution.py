import pytest
from solution import get_max_profit

# Tests
def test_single_stock():
    stock_prices = [9]
    with pytest.raises(Exception): get_max_profit(stock_prices)

def test_negative_profit():
    stock_prices = [11, 7, 6, 6, 10, 9]
    assert get_max_profit(stock_prices) == -1

def test_positive_profit():
    stock_prices = [10, 7, 5, 8, 11, 9]
    assert get_max_profit(stock_prices) == 6