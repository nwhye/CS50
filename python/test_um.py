from um import count

def test_count_middle():
    assert count("Hello, um, world") == 1


def test_count_beginning():
    assert count("um, hello world") == 1


def test_count_two():
    assert count("um, hello, um, world") == 2


def test_case():
    assert count("Um, um") == 2


def test_um():
    assert count("Um, drums, mum") == 1
