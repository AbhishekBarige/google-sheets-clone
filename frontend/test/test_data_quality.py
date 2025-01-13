import pytest
from services.data_quality import trim, upper, lower, remove_duplicates, find_and_replace

def test_trim():
    assert trim(['  hello ', ' world  ']) == ['hello', 'world']

def test_upper():
    assert upper(['hello', 'world']) == ['HELLO', 'WORLD']

