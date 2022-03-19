from src.hw4.node import Node


class CartesianTree:
    def __init__(self, nodes: dict):
        self.__nodes = nodes
        self.__root = self.__generate_child(sorted(nodes.items(), key=lambda x: x[0]))

        self.__iterator = None

    def __generate_child(self, available_nodes: list):
        """
        General complexity: O(n*log(n))

        :return: Generated child node with its child nodes.
        """

        if not available_nodes:
            return None

        node = Node(*max(available_nodes, key=lambda x: x[1]))

        left_part = available_nodes[: available_nodes.index((node.key, node.priority))]
        right_part = available_nodes[available_nodes.index((node.key, node.priority)) + 1 :]

        node.left_child = self.__generate_child(left_part)
        node.right_child = self.__generate_child(right_part)

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
            yield node
            if node.left_child:
                yield from visit_children(node.left_child)
            if node.right_child:
                yield from visit_children(node.right_child)

        self.__iterator = visit_children(self.__root)
        return self

    def __next__(self):
        return next(self.__iterator)

    def __contains__(self, key):
        """
        Complexity: O(log(n))
        """

        def find_key(node: Node) -> bool:
            if key == node.key:
                return True
            if key > node.key:
                if node.right_child:
                    return find_key(node.right_child)
                else:
                    return False

            if key < node.key:
                if node.left_child:
                    return find_key(node.left_child)
                else:
                    return False

        return find_key(self.__root)

    def __repr__(self):
        nodes_list = list(map(str, sorted(self.__nodes.items(), key=lambda x: x[0])))
        return "[" + ", ".join(nodes_list) + "]"
