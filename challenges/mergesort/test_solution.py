import pytest

# Import relevant functions from solution.py
from solution import merge_sort

# Tests
def test_order():
    array = [5,4,3,8,9,5,10,54,4]
    assert merge_sort(array) == [3, 4, 4, 5, 5, 8, 9, 10, 54]

def test_lengh():
    array = [5,4,3,8,9,5,10,54,4]
    assert len(merge_sort(array)) == len([3, 4, 4, 5, 5, 8, 9, 10, 54])

def test_empty():
    array = []
    assert merge_sort(array) == []

def test_even():
    array = [5,4,3,8,9,5,10,54,4,6]
    assert merge_sort(array) == [3, 4, 4, 5, 5, 6, 8, 9, 10, 54]