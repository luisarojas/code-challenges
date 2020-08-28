import pytest

# Import relevant functions from solution.py
from solution import check_orders

# Tests
def test_false():
    take_out_orders = [1, 3, 5]
    dine_in_orders = [2, 4, 6]
    served_orders = [1, 2, 4, 6, 5, 3]
    assert check_orders(take_out_orders, dine_in_orders, served_orders) == False

def test_true():
    take_out_orders = [17, 8, 24]
    dine_in_orders = [12, 19, 2]
    served_orders = [17, 8, 12, 19, 24, 2]
    assert check_orders(take_out_orders, dine_in_orders, served_orders) == True