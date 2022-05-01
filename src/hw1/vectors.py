import math
from collections.abc import Sequence


def get_inner_product(vector_a: Sequence, vector_b: Sequence):
    if len(vector_a) != len(vector_b):
        raise IndexError("Vectors dimensions are not equal")

    return sum([x * y for (x, y) in zip(vector_a, vector_b)])


def get_norm(vector: Sequence):
    return sum([x**2 for x in vector]) ** 0.5


def get_angle(vector_a: Sequence, vector_b: Sequence):
    if len(vector_a) != len(vector_b):
        raise IndexError("Vectors dimensions are not equal")

    cosine = get_inner_product(vector_a, vector_b) / (get_norm(vector_a) * get_norm(vector_b))
    assert -1 <= cosine <= 1, "Cosine limit exceeded"

    return math.acos(cosine)


if __name__ == "__main__":
    a = (1, 1.3, 3)
    b = [4, 5, 6]
    print(get_inner_product(a, b))
    print(get_norm(a))
    print(get_angle(a, b))
