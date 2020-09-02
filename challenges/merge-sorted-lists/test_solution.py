import pytest

# Import relevant functions from solution.py
from solution import merge

# Tests

def test_one_vs_many():
    a1 = [9]
    a2 = [1, 3, 5, 7, 14]
    expected = [1, 3, 5, 7, 9, 14]
    assert merge(a1, a2) == expected
    
def test_many_vs_one():
    a1 = [1, 3, 5, 7, 14]
    a2 = [9]
    expected = [1, 3, 5, 7, 9, 14]
    assert merge(a1, a2) == expected
    
def test_one_vs_one():
    a1 = [1]
    a2 = [9]
    expected = [1, 9]
    assert merge(a1, a2) == expected
    
def test_empty_vs_one():
    a1 = []
    a2 = [1]
    expected = [1]
    assert merge(a1, a2) == expected