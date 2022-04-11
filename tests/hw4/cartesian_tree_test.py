import pytest
from src.hw4.cartesian_tree import CartesianTree


def test_empty_tree():
    tree = CartesianTree()
    assert len(tree) == 0

    with pytest.raises(StopIteration):
        next(iter(tree))


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (dict(zip(range(5), "abcde")), "abcde"),
        (dict(list(zip([7, 0, 4, 9, 2, 11, 1, 10, 5, 6, 8, 3], "aceinnoorstv"))), "conversation"),
    ],
)
def test_creating_tree_by_dict(nodes, expected: str):
    tree = CartesianTree(nodes)
    print(nodes.items())

    assert len(tree) == len(nodes)
    assert list(iter(tree)) == list(zip(range(len(nodes)), expected))


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (dict(zip(range(5), "abcde")), "abcde"),
        (dict(list(zip([7, 0, 4, 9, 2, 11, 1, 10, 5, 6, 8, 3], "aceinnoorstv"))), "conversation"),
    ],
)
def test_creating_tree_by_inserts(nodes, expected):
    tree = CartesianTree()
    for key, value in nodes.items():
        tree[key] = value

    assert len(tree) == len(nodes)
    assert list(iter(tree)) == list(zip(range(len(nodes)), expected))


def test_change_value():
    tree = CartesianTree()
    tree[10] = "a"
    tree[15] = "b"
    tree[5] = "c"
    tree[5] = "d"
    assert len(tree) == 3
    assert tree[5] == "d"


def test_delete_value():
    tree = CartesianTree()
    tree[10] = "a"
    tree[15] = "b"
    tree[5] = "c"
    tree[20] = "d"
    tree[25] = "e"

    del tree[10]
    assert list(iter(tree)) == [(5, "c"), (15, "b"), (20, "d"), (25, "e")]

    del tree[25]
    assert list(iter(tree)) == [(5, "c"), (15, "b"), (20, "d")]

    with pytest.raises(KeyError):
        del tree[1]

    assert list(iter(tree)) == [(5, "c"), (15, "b"), (20, "d")]


def test_complex_interaction():
    tree = CartesianTree()
    tree[10] = "a"
    tree[15] = "b"
    tree[5] = "c"
    tree[5] = "d"
    del tree[10]
    with pytest.raises(KeyError):
        del tree[1]
    tree[20] = "e"
    tree[25] = "f"
    tree[25] = "g"
    del tree[25]
    tree[25] = "h"

    assert list(iter(tree)) == [(5, "d"), (15, "b"), (20, "e"), (25, "h")]

    del tree[5]
    del tree[15]
    del tree[20]
    del tree[25]

    assert list(iter(tree)) == []


def test_interaction_with_cleared_tree():
    tree = CartesianTree()
    tree[10] = "a"
    tree[15] = "b"
    tree[5] = "c"
    tree[5] = "d"
    tree.clear()
    assert len(tree) == 0
    assert list(iter(tree)) == []

    tree[10] = "a"
    tree[15] = "b"
    tree[5] = "c"
    tree[5] = "d"
    tree[20] = "e"
    tree[25] = "f"

    del tree[5]

    assert list(iter(tree)) == [(10, "a"), (15, "b"), (20, "e"), (25, "f")]
