from datetime import datetime
from functools import update_wrapper
from typing import Callable, List, Any, Tuple, Dict


class Spy:
    def __init__(self, function: Callable):
        update_wrapper(self, function)
        self._function = function
        self.logs: List[Tuple[str, Dict]] = []

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        current_time = str(datetime.now())
        params = {"args": args, "kwargs": kwargs}

        self.logs.append((current_time, params))
        return self._function(*args, **kwargs)


@Spy
def foo(num):
    print(num)


def print_usage_statistic(function: Callable):
    if not isinstance(function, Spy):
        raise ValueError("Function is not decorated with @Spy")

    for element in function.logs:
        yield element


if __name__ == '__main__':
    foo(30)
    foo("hello")
    foo(5)

    for (time, parameters) in print_usage_statistic(foo):
        str_parameters = ", ".join(
            f"{k} = {v}" for k, v in parameters.items()
        )
        print(
            f"function {foo.__name__} was called at {time} "
            f"with parameters:\n{str_parameters}"
        )
