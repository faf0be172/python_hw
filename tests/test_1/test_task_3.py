import pytest
from src.test_1.task_3 import reduce_right


def test_two_values_error():
    with pytest.raises(IndexError):
        reduce_right(lambda x, y: f"({x}+{y})", (ord(c) for c in "a"))


def test_simple_without_initial():
    result = reduce_right(lambda x, y: f"({x}+{y})", "abcde")
    assert result == "(a+(b+(c+(d+e))))"


def test_simple_with_initial():
    result = reduce_right(lambda x, y: f"({x}+{y})", "abcde", "initial")
    assert result == "(a+(b+(c+(d+(e+initial)))))"
