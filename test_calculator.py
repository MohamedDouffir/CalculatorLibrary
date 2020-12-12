"""
Unit tests for the calculator library
"""

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
