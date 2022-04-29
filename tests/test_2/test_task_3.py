from collections import Counter
from src.test_2.task_3 import process_file


def test_statistics():
    sentences_cnt, words_dict = process_file("text.txt")
    assert sentences_cnt == 9
    assert len(words_dict) == 84
    assert Counter(words_dict).most_common(5) == [("the", 13), ("in", 11), ("2", 11), ("of", 10), ("age", 10)]
