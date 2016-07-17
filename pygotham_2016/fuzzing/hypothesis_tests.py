import math
import cmath
from decimal import Decimal
import pytest

from hypothesis import given, settings
from hypothesis.strategies import *

primitive_strategies = [
    x() for x in [
        none, integers, booleans, complex_numbers, tuples, decimals,
        characters, text, binary, #fractions, randoms,
    ]
]

no_nan = [
    x(allow_nan=False) for x in [
        floats,
    ]
]

with_nan = [
    x() for x in [
        floats,
    ]
]


list_strategies = [
    x(one_of(primitive_strategies))
    for x in [
        frozensets, sets, lists,
    ]
]

dict_strategies = [
    x(one_of(primitive_strategies), one_of(primitive_strategies))
    for x in [
        dictionaries,
    ]
]

all_strategies = primitive_strategies + list_strategies + dict_strategies

def fuzz(nan=False):
    if nan:
        return one_of(primitive_strategies + with_nan + list_strategies + dict_strategies)
    return one_of(primitive_strategies + no_nan + list_strategies + dict_strategies)

def is_nan(l):
    def _is_nan(x):
        if isinstance(x, complex):
            return cmath.isnan(x)
        if isinstance(x, Decimal):
            return x.is_nan()
        return False
    return any(map(_is_nan, l))


@settings(max_examples=10000)
@given(fuzz())
def test_wat0(x):
    ''' Possible '''
    try:
        assert x == x
    except Exception as e:
        if isinstance(e, AssertionError) and not is_nan([x]):
            raise e



@settings(max_examples=1000)
@given(fuzz(), fuzz(), fuzz(), fuzz())
def test_wat1(x, a, b, c):
    # Not possible
    try:
        print "({}, {}, {}, {})".format(x, a, b, c)
        assert max(x) >= max(x[a:b:c])
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=500)
@given(fuzz(), fuzz())
def test_wat2(x, y):
    ''' Possible '''
    try:
        print "({}, {})".format(x, y)
        assert min(x, y) == min(y, x)
    except Exception as e:
        if isinstance(e, AssertionError) and not is_nan([x, y]):
            raise e


@settings(max_examples=1000)
@given(fuzz(), fuzz())
def test_wat3(x, y):
    # Not possible
    try:
        print "({}, {})".format(x, y)
        assert (any(x) and not any(x + y)) == False
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=1000)
@given(fuzz(), fuzz())
def test_wat4(x, y):
    ''' Possible '''
    try:
        print "({}, {})".format(x, y)
        assert x.count(y) <= len(x)
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=1000)
@given(one_of(integers(), floats()), integers(), integers())
def test_wat5(x, y, z):
    ''' Possible '''
    try:
        assert (x * (y * z)) == (x * y) * z
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=1000)
@given(fuzz(), fuzz())
def test_wat6(x, y):
    ''' Possible '''
    try:
        assert (x < y and all(a >= b for a, b in zip(x, y))) == False
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=1000)
@given(fuzz())
def test_wat7(x):
    # Not possible
    try:
        assert len(set(list(x))) == len(list(set(x)))
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=1000)
@given(fuzz())
def test_wat8(x):
    'Possible'
    try:
        assert min(x) == min(*x)
    except Exception as e:
        if isinstance(e, AssertionError):
            raise e


@settings(max_examples=100000)
@given(fuzz(), fuzz())
def test_wat9(x, y):
    # Not possible
    try:
        assert sum(0 * x, y) == y
    except Exception as e:
        if isinstance(e, AssertionError) and not is_nan([x, y]):
            raise e


@settings(max_examples=100000)
@given(fuzz(), fuzz())
def test_wat10(x, y):
    ''' Possible, but the fuzzer doesn't catch this one '''
    try:
        assert (y > max(x) and y in x) == False
    except Exception as e:
        if isinstance(e, AssertionError) and not is_nan([x, y]):
            raise e
