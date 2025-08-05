from bank import value

def test_hello():
    assert value("hello") == int(0)

def test_h():
    assert value("hey") == int(20)

def test_cap():
    assert value("HELLO") == int(0)
