from contextlib import contextmanager
from threading import Lock


class SafelyMultithreadingDict:

    def __init__(self):
        self._dict = {}
        self._locker = Lock()

    @contextmanager
    def modify_safely(self):
        """:return: Single-element generator with safely-modifying dictionary"""

        self._locker.acquire()
        try:
            yield self._dict
        finally:
            self._locker.release()
