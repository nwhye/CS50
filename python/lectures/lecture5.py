# --- UNIT TESTS
# assert - make sure something is true (boolean)

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:  # AssertionError because we use assert
        print("3 squared was not 9")


# this function located in another file, and can be imported as "from calculator import square"
# calculator is the name of the file where located function
def square(n):
    return n*n


if __name__ == "__main__":
    main()

# however this test code is so long that there no way someone would make it for every function
# so
# --- PYTEST - program, that automates test, as long as you write the test
# pip install pytest

import pytest

def test_square2():
    assert square(2) == 4  # no need to print try ans except as we use pytest
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# now instead of "python test.py", we write "pytest test.py"

# separating big test function to small ones (negative/positive, odd/even)


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def est_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0

# now lets test input


def test_str():
    with pytest.raises(TypeError):  # when "raised" error TypeError
        square("cat")  # when we pass "cat"

# -----------------------------------


def main():
    name = input("What's your name? ")
    print(hello(name))  # passing variable into the function and printing it


def hello(to="world"):
    # print("Hello " + to)  # however, we can't test when it's printing, as this is function not returning anything
    return f"hello, {to}"  # but we can test it if we return
# and in general better to return something, and not print, and printing would be handleled after import of this
# function   in any other program


# in another file:

def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("Hanna") == "hello, Hanna"
    # or
    for name in ["Hanna", "Danya", "Artem"]:  # how to use loops
        assert hello(name) == f"hello, {name}"


# the test must be small and simple, so we don't need test for tests

# to make folder not entering the folder "code test/test_hello.py"
# in directory with test we must create file "test/__init__/py"
# so we're telling to python that it must treat folder "test" as a package

# package is a module or moduls that are organised inside the folder

# now we can run "pytest test" - on a whole folder