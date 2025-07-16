#test_fuel.py

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("2/3") == 67

def test_non_digits():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("cat")

def test_negative_digits():
    with pytest.raises(ValueError):
        convert("-2/3")
        convert(" -2/3")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(45) == "45%"


'''
def test_convert() :
    assert convert("3/5") == 60
    assert convert("1/100") == 1
    assert convert("0/100") == 0
    assert convert("99/100") == 99
    assert convert("3/3") == 100
    with pytest.raises(ValueError):
        convert("2.8/3")
        convert("5/3")
        convert("-2/3")
        convert("2/-3")
        convert("Cat")
        convert("Dog/Cat")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
'''
