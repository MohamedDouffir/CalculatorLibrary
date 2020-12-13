from pytest import fixture


@fixture
def mult_testdata():
    return {12: (4, 3), 24: (8, 3), 36: (9, 4)}


@fixture
def power_testdata():
    return {8: (2, 3), 125: (5, 3), 27: (3, 3)}
