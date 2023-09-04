# test_calculator.py
import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_sub():
    assert calculator.sub(5, 2) == 3

def test_mul():
    assert calculator.mul(4, 6) == 24

def test_div():
    assert calculator.div(8, 4) == 2
