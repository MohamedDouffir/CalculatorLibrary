import math
"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    return first_term / second_term


def square_root(aNumber):
    return math.sqrt(aNumber)


def power(base, exponent):
    return math.pow(base, exponent)


def cosine(x):
    """ It returns the cosine of x radians using
    Python math module method cos() """
    return math.cos(x)


def sine(x):
    """ It returns the sine of x in radians using
    Python math module method sin() """
    return math.sin(x)
