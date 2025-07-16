# test_um.py
from um import count
import pytest

def test_1():
    assert count("um") == 1

def test_2():
    assert count("um?") == 1

def test_3():
    assert count("Um, thanks for the album.") == 1

def test_4():
    assert count("Um, thanks, um...") == 2

def test_5():
    assert count("umy") == 0

def test_6():
    assert count("yummy") == 0
