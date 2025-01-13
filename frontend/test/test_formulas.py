import pytest
from services.formulas import sum_range, average

def test_sum_range():
    assert sum_range([1, 2, 3, 4, 5]) == 15

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
