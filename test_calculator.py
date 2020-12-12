"""
Unit tests for the calculator library
"""
import math
import calculator
from pytest import mark


class TestCalculator:

    @mark.add
    def test_addition1(self):
        assert 4 == calculator.add(2, 2)

    @mark.add
    def test_addition2(self):
        assert 20 == calculator.add(14, 6)

    @mark.sub
    def test_subtraction1(self):
        assert 2 == calculator.subtract(4, 2)

    @mark.sub
    def test_subtraction2(self):
        assert 6 == calculator.subtract(20, 14)

    @mark.mult
    def test_multiplication1(self):
        assert 100 == calculator.multiply(10, 10)

    @mark.mult
    def test_multiplication2(self):
        assert 36 == calculator.multiply(9, 4)

    @mark.div
    def test_division1(self):
        assert 100 == calculator.divide(1000, 10)

    @mark.div
    def test_division2(self):
        assert 25 == calculator.divide(125, 5)

    @mark.power
    def test_square_root(self):
        assert 5 == calculator.square_root(25)

    @mark.power
    def test_power(self):
        assert 8 == calculator.power(2, 3)

    @mark.trig
    def test_cosine(self):
        assert 1.0 == calculator.cosine(0)
        assert -1.0 == calculator.cosine(math.pi)

    @mark.trig
    def test_sine(self):
        assert 0.0 == calculator.sine(0)
        assert 1.0 == calculator.sine(math.pi/2)
