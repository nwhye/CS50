from twttr import shorten

def test_lower():
    assert shorten("Twitter") == "Twttr"

def test_cap():
    assert shorten("SMASH") == "SMSH"

def test_punctuation():
    assert shorten("Hello World!") == "Hll Wrld!"

def test_numbers():
    assert shorten("CS50") == "CS50"
