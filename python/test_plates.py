from plates import is_valid

def test_twoletters():
    assert is_valid("HELLO") == True


def test_noalpha():
    assert is_valid("50") == False


def test_length():
    assert is_valid("HELLOOOO") == False


def test_numberplace():
    assert is_valid("CS50P") == False


def test_num():
    assert is_valid("CS05") == False


def test_Alphanum():
    assert is_valid("PI3.14") == False
