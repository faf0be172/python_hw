from threading import Thread
from src.hw3.semaphore import SafelyMultithreadingDict


def replace_or_create_pair(dictionary: SafelyMultithreadingDict, key: str, value: int):
    with dictionary.modify_safely() as dct:
        dct[key] = value


def change_pair(dictionary: SafelyMultithreadingDict, key: str, diff: int):
    with dictionary.modify_safely() as dct:
        dct[key] += diff


def test_multithreaded_creating_pairs():
    testing_dict = SafelyMultithreadingDict()
    threads = [
        Thread(target=replace_or_create_pair, args=(testing_dict, f"key_{number}", number**2))
        for number in range(1, 6)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    with testing_dict.modify_safely() as d:
        for number in range(1, 6):
            assert d[f"key_{number}"] == number**2


def test_multithreading_change_pair():
    testing_dict = SafelyMultithreadingDict()
    replace_or_create_pair(testing_dict, "key_1", 0)

    threads = [
        Thread(target=change_pair, args=(testing_dict, "key_1", number * 2)) for number in range(1, 6)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    with testing_dict.modify_safely() as d:
        assert d["key_1"] == 30
