import pytest
from src.test_1.task_1 import print_usage_statistic, Spy


def test_func_not_decorated():

    with pytest.raises(ValueError):
        def foo():
            return "abc"

        for (_, _) in print_usage_statistic(foo):
            pass


def test_func_without_call():
    @Spy
    def foo():
        return "abc"

    result = []
    for (_, params) in print_usage_statistic(foo):
        result.append(params)

    assert len(result) == 0


def test_func_time_not_null():
    @Spy
    def foo():
        return "abc"

    foo()
    foo()

    result = []
    for (time, _) in print_usage_statistic(foo):
        result.append(time)

    # print(result)

    assert type(result[0]) == str
    assert type(result[1]) == str


def test_func_with_args():
    @Spy
    def foo(arg):
        return arg

    foo("abc")
    foo("def")

    result = []
    for _, parameters in print_usage_statistic(foo):
        result.append(parameters)

    assert result == [{"args": ("abc",), "kwargs": {}}, {"args": ("def",), "kwargs": {}}]


def test_func_with_kwargs():
    @Spy
    def foo(kwarg):
        return kwarg

    foo(kwarg="abc")
    foo(kwarg="def")

    result = []
    for _, parameters in print_usage_statistic(foo):
        result.append(parameters)

    assert result == [{"args": (), "kwargs": {"kwarg": "abc"}}, {"args": (), "kwargs": {"kwarg": "def"}}]
