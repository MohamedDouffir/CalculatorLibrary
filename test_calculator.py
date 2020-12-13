"""
Unit tests for the calculator library
"""
import math
import calculator
from pytest import mark


class TestCalculator:

    @mark.smoke
    @mark.add
    def test_addition1(self):
        assert 4 == calculator.add(2, 2)

    @mark.add
    def test_addition2(self):
        assert 20 == calculator.add(14, 6)

    @mark.smoke
    @mark.sub
    def test_subtraction1(self):
        assert 2 == calculator.subtract(4, 2)

    @mark.sub
    def test_subtraction2(self):
        assert 6 == calculator.subtract(20, 14)

    @mark.smoke
    @mark.mult
    def test_multiplication1(self, mult_testdata):
        d = mult_testdata
        for p in d.keys():
            v1 = d[p][0]
            v2 = d[p][1]
            assert p == calculator.multiply(v1, v2)

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
    def test_power(self, power_testdata):
        d = power_testdata
        for p in d.keys():
            base = d[p][0]
            expo = d[p][1]
            assert p == calculator.power(base, expo)

    @mark.trig
    def test_cosine(self):
        assert 1.0 == calculator.cosine(0)
        assert -1.0 == calculator.cosine(math.pi)

    @mark.trig
    def test_sine(self):
        assert 0.0 == calculator.sine(0)
        assert 1.0 == calculator.sine(math.pi/2)
