from math_ops import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20
from math_ops import divide

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
