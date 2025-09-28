from seasons import Born
import pytest

def test_validation():
    with pytest.raises(SystemExit):
        Born.validate("Jun 19, 1990")

def test_convert():
    assert Born.convert("2002-07-10") == "Twenty million, twenty thousand, seven hundred ten minutes"
