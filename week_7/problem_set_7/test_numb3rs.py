# test_numb3rs.py

from numb3rs import validate

def test_ip_0_255():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("127.00.0.1") == False
    assert validate("000.1.0.1") == False

def test_ip_with_str():
    assert validate("cat") == False

def test_ip_without_0():
    assert validate("128.200.1.15") == True

def test_ip_greater_than_255():
    assert validate("257.2.3.100") == False

