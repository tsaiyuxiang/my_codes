# test_twttr.py

from twttr import shorten

def test_twttr():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50P") == "CS50P"
    assert shorten("12345") == "12345"
    assert shorten("#$-&￥") == "#$-&￥"
