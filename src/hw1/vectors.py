import math


def get_inner_product(vector_a, vector_b):
    if type(vector_a) not in [tuple, list]:
        raise TypeError("First vector must be list or tuple")
    if type(vector_b) not in [tuple, list]:
        raise TypeError("Second vector must be list or tuple")
    if len(vector_a) != len(vector_b):
        raise IndexError("Vectors dimensions are not equal")

    try:
        product = sum([x * y for (x, y) in zip(vector_a, vector_b)])
    except TypeError as error:
        raise ArithmeticError("Values inside could not be multiplied") from error
    else:
        assert type(product) in [int, float], "Product is not a number"
        return product


def get_norm(vector):
    if type(vector) not in [tuple, list]:
        raise TypeError("Vector must be list or tuple")
    try:
        vector_norm = sum([x**2 for x in vector]) ** 0.5
    except TypeError as error:
        raise ArithmeticError("Values inside could not be multiplied") from error
    else:
        assert type(vector_norm) in [int, float], "Norm is not a number"
        assert vector_norm >= 0, "Norm are negative"
        return vector_norm


def get_angle(vector_a, vector_b):
    if type(vector_a) not in [tuple, list]:
        raise TypeError("First vector must be list or tuple")
    if type(vector_b) not in [tuple, list]:
        raise TypeError("Second vector must be list or tuple")
    if len(vector_a) != len(vector_b):
        raise IndexError("Vectors dimensions are not equal")

    try:
        cosine = get_inner_product(vector_a, vector_b) / (get_norm(vector_a) * get_norm(vector_b))
        assert -1 <= cosine <= 1, "Cosine limit exceeded"
        angle = math.acos(cosine)

    except TypeError as error:
        raise ArithmeticError("Values inside could not be multiplied") from error
    else:
        assert type(angle) in [int, float], "Angle is not a number"
        return angle


if __name__ == "__main__":
    a = (1, 1.3, 3)
    b = [4, 5, 6]
    print(get_inner_product(a, b))
    print(get_norm(a))
    print(get_angle(a, b))
