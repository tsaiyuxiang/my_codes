# test_seasons.py
from seasons import convert
import pytest

def test_1():
    assert convert("2020-04-18") == "Two million, seven hundred fifty-seven thousand, six hundred minutes"

def test_2():
    assert convert("2020-04-31") == "Invalid date"

def test_5():
    with pytest.raises(SystemExit):
        convert("February 6th, 1998")
