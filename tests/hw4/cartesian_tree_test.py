import pytest
from src.hw4.cartesian_tree import CartesianTree


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (dict(zip(range(5), [2, 4, 0, 9, 7])), [(3, 9), (1, 4), (0, 2), (2, 0), (4, 7)]),
        (
            dict(zip(range(10), [23, 24, 22, 30, 28, 27, 29, 21, 26, 25])),
            [(3, 30), (1, 24), (0, 23), (2, 22), (6, 29), (4, 28), (5, 27), (8, 26), (7, 21), (9, 25)],
        ),
        (
            dict(zip(range(11), [11, 17, 13, 19, 12, 8, 10, 0, 5, 2, 15])),
            [(3, 19), (1, 17), (0, 11), (2, 13), (10, 15), (4, 12), (6, 10), (5, 8), (8, 5), (7, 0), (9, 2)],
        ),
    ],
)
def test_creating_tree(nodes, expected):
    tree = CartesianTree(nodes)
    iterator = iter(tree)

    nlr_result = [(node.key, node.priority) for node in iterator]
    assert nlr_result == expected


@pytest.mark.parametrize(
    "nodes",
    [
        dict(zip(range(10), [23, 24, 22, 30, 28, 27, 29, 21, 26, 25])),
        dict(zip(range(11), [11, 17, 13, 19, 12, 8, 10, 0, 5, 2, 15])),
    ],
)
@pytest.mark.parametrize(
    "key, expected",
    [
        (0, True),
        (5, True),
        (9, True),
        (100, False),
        (-1, False),
    ],
)
def test_contains_operator(nodes, key, expected):
    tree = CartesianTree(nodes)
    assert (key in tree) == expected


@pytest.mark.parametrize(
    "nodes, expected",
    [
        (dict(zip(range(5), [2, 4, 0, 9, 7])), "[(0, 2), (1, 4), (2, 0), (3, 9), (4, 7)]"),
        (
            dict(zip(range(10), [23, 24, 22, 30, 28, 27, 29, 21, 26, 25])),
            "[(0, 23), (1, 24), (2, 22), (3, 30), (4, 28), (5, 27), (6, 29), (7, 21), (8, 26), (9, 25)]",
        ),
        (
            dict(zip(range(11), [11, 17, 13, 19, 12, 8, 10, 0, 5, 2, 15])),
            "[(0, 11), (1, 17), (2, 13), (3, 19), (4, 12), (5, 8), (6, 10), (7, 0), (8, 5), (9, 2), (10, 15)]",
        ),
    ],
)
def test_tree_representation(nodes, expected):
    tree = CartesianTree(nodes)
    assert repr(tree) == expected
