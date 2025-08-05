from fuel import convert, gauge
import pytest

def test_c_num():
    assert convert("4/4") == 100


def test_c_valer():
    with pytest.raises(ValueError):
        convert("cat/cat")
    with pytest.raises(ValueError):
        convert("-4/4")

def test_c_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_g():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
