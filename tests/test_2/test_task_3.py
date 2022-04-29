import os
from collections import Counter
from src.test_2.task_3 import process_file


def test_statistics():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    conf_path = os.path.join(dir_path, "text.txt")

    sentences_cnt, words_dict = process_file(conf_path)
    assert sentences_cnt == 9
    assert len(words_dict) == 84
    assert Counter(words_dict).most_common(5) == [("the", 13), ("in", 11), ("2", 11), ("of", 10), ("age", 10)]
