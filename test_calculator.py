"""
Unit tests for the calculator library
"""
import math
import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 100 == calculator.divide(1000, 10)

    def test_square_root(self):
        assert 5 == calculator.square_root(25)

    def test_power(self):
        assert 8 == calculator.power(2, 3)

    def test_cosine(self):
        assert 1.0 == calculator.cosine(0)
        assert -1.0 == calculator.cosine(math.pi)

    def test_sine(self):
        assert 0.0 == calculator.sine(0)
        assert 1.0 == calculator.sine(math.pi/2)
