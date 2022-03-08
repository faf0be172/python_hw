import pytest
from src.hw2.curry import curry_explicit, uncurry_explicit
from typing import Callable


@pytest.mark.parametrize(
    "func, args, arity, expected",
    [
        (lambda x, y, z: f"<{x},{y},{z}>", (123, 456, 562), 3, "<123,456,562>"),
        (max, (10, 11), 2, 11),
        (len, ([1, 2],), 1, 2)
    ],
)
def test_currying(func: Callable, args: tuple, arity: int, expected):
    result = curry_explicit(func, arity)
    for cnt in range(arity):
        result = result(args[cnt])
    assert result == expected


@pytest.mark.parametrize(
    "func, args, arity, expected",
    [
        (lambda x, y, z: f"<{x},{y},{z}>", (123, 456, 562), 3, "<123,456,562>"),
        (max, (10, 11), 2, 11),
        (len, ([1, 2],), 1, 2)
    ],
)
def test_uncurrying(func: Callable, args: tuple, arity: int, expected):
    curried_func = curry_explicit(func, arity)
    uncurried_func = uncurry_explicit(curried_func, arity)
    assert uncurried_func(*args) == expected


def test_curry_zero_arity():
    curried_func = curry_explicit(lambda: 1, 0)
    assert curried_func() == 1


def test_uncurry_zero_arity():
    curried_func = curry_explicit(max, 3)
    uncurried_func = uncurry_explicit(curried_func, 0)
    assert uncurried_func()(1)(2)(3) == 3


def test_curry_negative_arity():
    with pytest.raises(TypeError):
        curry_explicit(max, -1)


def test_uncurry_negative_arity():
    curried_func = curry_explicit(max, 2)
    with pytest.raises(TypeError):
        uncurry_explicit(curried_func, -1)


def test_curry_too_many_args():
    with pytest.raises(TypeError):
        curried_func = curry_explicit(max, 2)
        curried_func(1)(2)(3)


def test_curry_lack_of_args():
    try:
        curried_func = curry_explicit(max, 2)
        curried_func(1)
    except TypeError:
        raise AssertionError("TypeError exception has been raised")


def test_uncurry_lack_of_arguments():
    curried_func = curry_explicit(max, 3)
    uncurried_func = uncurry_explicit(curried_func, 3)
    with pytest.raises(TypeError):
        uncurried_func(1, 2)


def test_uncurry_too_many_arguments():
    curried_func = curry_explicit(max, 3)
    uncurried_func = uncurry_explicit(curried_func, 3)
    with pytest.raises(TypeError):
        uncurried_func(1, 2, 3, 4)


def test_freeze_print_arity():
    curried_print = curry_explicit(print, 2)
    assert curried_print(1)(2) is None
