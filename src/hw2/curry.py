from typing import Callable


def curry_explicit(func: Callable, arity: int) -> Callable:
    """:return: Curried function with arity = 1  """

    if arity < 0:
        raise TypeError("Negative arity forbidden")

    if 0 <= arity <= 1:
        return func

    def curried_func(arg) -> Callable:
        def simplified_func(*args):
            """:return: Original function with fixed first arguments"""
            if len(args) != arity - 1:
                raise TypeError("Entered arity doesn't match with the number of arguments")
            return func(arg, *args)

        return curry_explicit(simplified_func, arity - 1)

    return curried_func


def uncurry_explicit(curried_func: Callable, arity: int) -> Callable:
    """:return: Function with entered arity"""
    if arity < 0:
        raise TypeError("Negative arity forbidden")

    def uncurried_function(*args) -> Callable:
        if len(args) != arity:
            raise TypeError("Uncurried function arity doesn't match with the number of arguments")

        constructing_function = curried_func
        for arg in args:
            """Arguments are applied step by step"""
            constructing_function = constructing_function(arg)

        return constructing_function

    return uncurried_function
