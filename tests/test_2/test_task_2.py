from random import shuffle, randint

from src.test_2.task_2 import quicksort


def test_simple_sorting():
    numbers = [1, 1, 2, 2, 5, 6, 7, 8, 9, 10]
    shuffle(numbers)
    sorted_numbers = sorted(numbers)

    assert sorted_numbers == quicksort(numbers)


def test_random_list_sorting():
    numbers = [num for num in [randint(1, 100000) for _ in range(20)]]

    assert sorted(numbers) == quicksort(numbers)


def test_empty_list():
    assert [] == quicksort([])


def test_sorted_list():
    assert [1, 2, 3] == quicksort([1, 2, 3])
