class Node:
    def __init__(self, key: int, priority: int):
        self.key = key
        self.priority = priority

        self.left_child = None
        self.right_child = None
