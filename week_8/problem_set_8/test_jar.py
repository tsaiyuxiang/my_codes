# test_jar.py
from jar import Jar
import pytest

def test_init():
    jar1 = Jar(15)
    assert jar1.capacity == 15
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar1 = Jar(0)
        jar2 = Jar(-1)

def test_1():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

def test_str():
    jar1 = Jar(10)
    assert jar1.capacity == 10
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar1 = Jar(10)
    assert jar1.capacity == 10
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar1.deposit(1)

def test_withdraw():
    jar1 = Jar(10)
    assert str(jar1) == ""
    jar1.deposit(5)
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.withdraw(4)
    assert str(jar1) == "🍪"
    with pytest.raises(ValueError):
        jar1.withdraw(2)

