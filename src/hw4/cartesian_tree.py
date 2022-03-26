from random import randint
from typing import Any

MAX_TREE_KEY = int(10e9)


class Node:
    def __init__(self, key: int, value, priority: int):
        self.key = key
        self.value = value
        self.priority = priority
        self.left_child = None
        self.right_child = None

    def __iter__(self):
        def visit_children(node: Node):
            """
            :return: Generator of LNR-traversal nodes sequence.
            """

            if node.left_child:
                yield from visit_children(node.left_child)

            yield node

            if node.right_child:
                yield from visit_children(node.right_child)

        return visit_children(self)

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

    @staticmethod
    def split(node, key: int) -> tuple[Any, Any]:
        if node is None:
            return None, None

        if key > node.key:
            left, right = Node.split(node.right_child, key)
            node.right_child = left
            return node, right

        elif key < node.key:
            left, right = Node.split(node.left_child, key)
            node.left_child = right
            return left, node

        else:
            return node.left_child, node.right_child

    @staticmethod
    def merge(node_a, node_b):
        if node_a is None:
            return node_b

        if node_b is None:
            return node_a

        if node_a.priority > node_b.priority:
            node_a.right_child = Node.merge(node_a.right_child, node_b)
            return node_a

        else:
            node_b.left_child = Node.merge(node_a, node_b.left_child)
            return node_b


class CartesianTree:
    def __init__(self, nodes_values=None):
        if nodes_values is None:
            nodes_values = {}

        self._size = 0
        self._root = None
        if len(nodes_values) > 0:
            self._size = len(nodes_values)
            nodes = [(key, value, randint(1, MAX_TREE_KEY)) for key, value in nodes_values.items()]

            def generate_child(available_nodes: list[tuple[int, Any, int]]):
                if not available_nodes:
                    return None

                node = Node(*max(available_nodes, key=lambda x: x[2]))

                left_part = available_nodes[: available_nodes.index((node.key, node.value, node.priority))]
                right_part = available_nodes[available_nodes.index((node.key, node.value, node.priority)) + 1:]

                node.left_child = generate_child(left_part)
                node.right_child = generate_child(right_part)

                return node

            self._root = generate_child(sorted(nodes, key=lambda x: x[0]))

    def __iter__(self):
        if not self._root:
            return iter([])

        for node in self._root:
            yield node.key, node.value

    def __contains__(self, key: int):
        node = self._root.find_node(key)
        return node is not None

    def __len__(self):
        return self._size

    def __getitem__(self, key: int):
        node = self._root.find_node(key)

        if node is None:
            raise KeyError(f"Key {key} not found")

        return node.value

    def __setitem__(self, key: int, value: Any):
        if self._root:
            entry = self._root.find_node(key)
            if entry:
                entry.value = value

            else:
                def insert(node: Node):
                    left, right = Node.split(self._root, node.key)
                    self._root = Node.merge(Node.merge(left, node), right)

                insert(Node(key, value, randint(1, MAX_TREE_KEY)))
                self._size += 1

        else:
            self._root = Node(key, value, randint(1, MAX_TREE_KEY))
            self._size += 1

    def __delitem__(self, key: int):
        node = self._root.find_node(key)

        if node:
            def delete():
                left, right = Node.split(self._root, key)
                self._root = Node.merge(left, right)

            delete()
            self._size -= 1

        else:
            raise KeyError(f"Key '{key}' not found")

    def __repr__(self):
        items = [f"{key}: {repr(value)}" for key, value in self]
        return self.__class__.__name__ + ": {" + ", ".join(items) + "}"

    def clear(self):
        self._size = 0
        self._root = None
