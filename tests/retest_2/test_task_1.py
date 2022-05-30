import os
import warnings

from src.retest_2.task_1 import logger


def test_single_call():
    log_file_path = "logs.txt"
    warnings.simplefilter("ignore")

    @logger(log_file_path)
    def get_const(*args):
        return 17

    get_const(1, "abc")

    try:
        with open(log_file_path) as logs_file:
            lines = logs_file.readlines()
            assert len(lines) == 1 and lines[0].endswith("get_const (1, 'abc') ({}) 17 \n")
    finally:
        os.remove(log_file_path)


def test_repeated_call():
    log_file_path = "logs.txt"
    warnings.simplefilter("ignore")

    @logger(log_file_path)
    def f(n):
        if n != 0:
            f(n - 1)

    f(1)

    try:
        with open(log_file_path) as logs_file:
            lines = logs_file.readlines()
            assert len(lines) == 2
            assert lines[0].endswith("f (0,) ({}) None \n")
            assert lines[1].endswith("f (1,) ({}) None \n")
    finally:
        os.remove(log_file_path)
