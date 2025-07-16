# test_bank.py

from bank import value

def test_bank():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("heLlO") == 0
    assert value("hello guys") == 0
    assert value("Hey") == 20
    assert value("Good day guys") == 100
    assert value(" ") == 100





