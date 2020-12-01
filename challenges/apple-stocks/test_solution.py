import pytest
from solution import get_max_profit

# Tests
def test_single_stock():
	stock_prices = [9]
	assert get_max_profit(stock_prices) == 0
	# with pytest.raises(SingleStockPrice): get_max_profit(stock_prices)

# def test_negative_profit():
#     stock_prices = [11, 7, 6, 6, 10, 9]
#     assert get_max_profit(stock_prices) == -1

def test_positive_profit():
	stock_prices = [10, 7, 5, 8, 11, 9]
	assert get_max_profit(stock_prices) == 6

def test_no_gain():
	stock_prices = [7,6,4,3,1]
	assert get_max_profit(stock_prices) == 0

def test_empty_sequence():
	stock_prices = []
	assert get_max_profit(stock_prices) == 0

def test_multiple_max_prices():
	stock_prices = [2,1,2,1,0,1,2]
	assert get_max_profit(stock_prices) == 2

def test_max_before_min_1():
	stock_prices = [3,3,5,0,0,3,1,4]
	assert get_max_profit(stock_prices) == 4

def test_max_before_min_2():
	stock_prices = [3,2,6,5,0,3]
	assert get_max_profit(stock_prices) == 4