from src.hw4.node import Node


class CartesianTree:
    def __init__(self, nodes: dict):
        self.__nodes = nodes
        self.__root = self.__generate_child(sorted(nodes.items(), key=lambda x: x[0]), parent=None)

        self.__iterator = None

    def __generate_child(self, available_nodes: list, parent):
        """
            General complexity: O(n*log(n))

            :return: Generated child node with its child nodes.
        """

        if not available_nodes:
            return None

        node = Node(*max(available_nodes, key=lambda x: x[1]))

        left_part = available_nodes[:available_nodes.index((node.key, node.priority))]
        right_part = available_nodes[available_nodes.index((node.key, node.priority)) + 1:]

        node.left_child = self.__generate_child(left_part, node)
        node.right_child = self.__generate_child(right_part, node)

        return node

    def __iter__(self):
        """
            Refresh local iterator by setting root node to the first element in sequence.

            :return: Refreshed instance.
        """

        def visit_children(node: Node):
            """
                :param node: Current node in NLR traversal.
                :return: Generator of NLR-traversal nodes sequence.
            """
            if node:
                yield node
                yield from visit_children(node.left_child)
                yield from visit_children(node.right_child)

        self.__iterator = visit_children(self.__root)
        return self

    def __next__(self):
        return next(self.__iterator)

    def __contains__(self, key):
        iterator = iter(self)
        for node in iterator:
            if node.key == key:
                return True
        return False
