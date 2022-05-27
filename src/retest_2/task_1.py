import inspect
import os.path
import warnings
from datetime import datetime
from typing import Callable


def logger(logs_file_name: str):
    def outer_wrapper(func: Callable):
        if inspect.isclass(func):
            raise ValueError("Logger works with function")

        if not os.path.exists(logs_file_name):
            warnings.warn(f"New file {logs_file_name} will be created", ResourceWarning)

        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(logs_file_name, "a") as log_file:
                log_file.write(f"{datetime.now()} {func.__name__} {args} ({kwargs}) {result} \n")

            return result

        return inner_wrapper

    return outer_wrapper
