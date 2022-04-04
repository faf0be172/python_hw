from typing import Callable, Any


def reduce_right(function: Callable, values: Any, initial: Any = None):
    args = [element for element in values]
    if initial is not None:
        args.append(initial)
    args.reverse()

    if len(args) <= 1:
        raise IndexError("At least two values needed")

    final_value = function(args[1], args[0])

    for arg in args[2:]:
        final_value = function(arg, final_value)

    return final_value
