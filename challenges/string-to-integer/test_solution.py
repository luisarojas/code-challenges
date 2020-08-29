import pytest

# Import relevant functions from solution.py
from solution import my_atoi

def test_space_minus():
    assert my_atoi("   -42") == -42
    
def test_words_before():
    assert my_atoi("words and 987") == 0
    
def test_words_after():
    assert my_atoi("4193 with words") == 4193
    
def test_under_min():
    assert my_atoi("-91283472332") == -2147483648