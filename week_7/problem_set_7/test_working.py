# test_working.py
from working import convert
import pytest

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:23 AM to 5:35 PM") == "09:23 to 17:35"

def test_2():
    with pytest.raises(ValueError):
        convert("14 AM to 5 PM")

def test_3():
    with pytest.raises(ValueError):
        convert("12 AM to 5:60 PM")

def test_4():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_5():
    with pytest.raises(ValueError):
        convert("9 to 5")
        convert("5 AM to 17:00")
        convert("17:00 to 9 PM")


'''
def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("09 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 05 AM") == "21:00 to 05:00"

def test_2():
    assert convert("9:01 AM to 5:23 PM") == "09:01 to 17:23"
    assert convert("09:01 AM to 5:23 PM") == "09:01 to 17:23"
    assert convert("9:12 PM to 05:45 AM") == "21:12 to 05:45"

def test_error_1():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("9:02 AM - 5:23 PM")
        convert("9 AM 5 PM")
        convert("9 to 5 PM")
        convert("9 AM to 5")
        convert("9  AM to 5 PM")
        convert("9 AM to 5  PM")
        convert("Cat")

def test_error_2():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("9 AM to 13 PM")
        convert("9:60 AM to 5:23 PM")
        convert("9:20 AM to 5:61 PM")

def test_error_3():
    with pytest.raises(ValueError):
        convert("9:5 AM to 5:23 PM")
        convert("9:23 AM to 5:9 PM")
'''
