from random import randint
from typing import Any, Tuple, Optional


class CartesianTreeNode:
    def __init__(self, key: int, value: Any, priority_limit: int = int(10e9)):
        self.key = key
        self.value = value
        self.priority = randint(1, priority_limit)
        self.left_child = None
        self.right_child = None

    def __iter__(self):
        """
        :return: Generator of LNR-traversal nodes sequence.
        """

        if self.left_child:
            yield from self.left_child

        yield self

        if self.right_child:
            yield from self.right_child

    def find_node(self, key: int):
        """
        Search the node with given key down the tree.
        """

        if key < self.key:
            if self.left_child is None:
                return None
            return self.left_child.find_node(key)

        elif key > self.key:
            if self.right_child is None:
                return None
            return self.right_child.find_node(key)

        else:
            return self


class CartesianTree:
    def __init__(self, nodes_values=None, priority_limit: int = int(10e9)):
        if nodes_values is None:
            nodes_values = {}

        self._size = 0
        self._root: Optional[CartesianTreeNode] = None
        self._priority_limit = priority_limit

        if len(nodes_values) > 0:
            for key, value in nodes_values.items():
                self[key] = value

    def __iter__(self):
        if not self._root:
            return iter([])

        for node in self._root:
            yield node.key, node.value

    def __contains__(self, key: int):
        if self._root:
            node = self._root.find_node(key)
            return node is not None
        else:
            return False

    def __len__(self):
        return self._size

    def __getitem__(self, key: int):
        if self._root:
            node = self._root.find_node(key)
            if node is None:
                raise KeyError(f"Key {key} not found")
            return node.value
        else:
            raise KeyError(f"Key {key} not found, tree is empty")

    def __setitem__(self, key: int, value: Any):
        if self._root:
            entry = self._root.find_node(key)
            if entry:
                entry.value = value

            else:
                node = CartesianTreeNode(key, value, self._priority_limit)
                left, right = self.split(self._root, node.key)
                self._root = self.merge(self.merge(left, node), right)
                self._size += 1

        else:
            self._root = CartesianTreeNode(key, value, self._priority_limit)
            self._size += 1

    def __delitem__(self, key: int):
        if self._root:
            node = self._root.find_node(key)
            if node:
                left, right = self.split(self._root, key)
                self._root = self.merge(left, right)
                self._size -= 1
            else:
                raise KeyError(f"Key '{key}' not found")

        else:
            raise KeyError(f"Key '{key}' not found, tree is empty")

    def __repr__(self):
        items = [f"{key}: {repr(value)}" for key, value in self]
        return self.__class__.__name__ + ": {" + ", ".join(items) + "}"

    def clear(self):
        self._size = 0
        self._root = None

    def split(self, node, key: int) -> Tuple[Any, Any]:
        if node is None:
            return None, None

        if key > node.key:
            left, right = self.split(node.right_child, key)
            node.right_child = left
            return node, right

        elif key < node.key:
            left, right = self.split(node.left_child, key)
            node.left_child = right
            return left, node

        else:
            return node.left_child, node.right_child

    def merge(self, node_a, node_b):
        if node_a is None:
            return node_b

        if node_b is None:
            return node_a

        if node_a.priority > node_b.priority:
            node_a.right_child = self.merge(node_a.right_child, node_b)
            return node_a

        else:
            node_b.left_child = self.merge(node_a, node_b.left_child)
            return node_b
