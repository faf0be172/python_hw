from numbers import Number
from typing import Sequence, List


def validate_matrix(matrix: Sequence[Sequence[Number]]):
    assert len({len(row) for row in matrix}) == 1, "Matrix is invalid"


def get_transpose(matrix: Sequence[Sequence[Number]]) -> List[List[Number]]:
    validate_matrix(matrix)
    transposed_matrix = [list(row) for row in list(zip(*matrix))]
    validate_matrix(transposed_matrix)

    assert len(transposed_matrix) == len(matrix[0]) and len(transposed_matrix[0]) == len(matrix), \
        "Result matrix dimension is invalid"
    return transposed_matrix


def get_matrices_sum(matrix_a: Sequence[Sequence[Number]], matrix_b: Sequence[Sequence[Number]]) -> List[List[Number]]:
    validate_matrix(matrix_a)
    validate_matrix(matrix_b)

    if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
        result = [list(x + y for (x, y) in zip(row_a, row_b)) for row_a, row_b in zip(matrix_a, matrix_b)]
        validate_matrix(result)

        assert len(result) == len(matrix_a) and len(result[0]) == len(matrix_a[0]), "Result matrix dimension is invalid"
        return result
    else:
        raise TypeError("Matrices dimensions are not equal")


def get_matrices_product(matrix_a: Sequence[Sequence[Number]], matrix_b: Sequence[Sequence[Number]]) -> \
        List[List[Number]]:
    validate_matrix(matrix_a)
    validate_matrix(matrix_b)

    assert len(matrix_a[0]) == len(matrix_b), "Matrices could not be multiplied"

    transposed_matrix_b = get_transpose(matrix_b)
    validate_matrix(transposed_matrix_b)

    result = [list(sum(x * y for (x, y) in zip(row_a, row_b)) for row_b in transposed_matrix_b) for row_a in matrix_a]

    validate_matrix(result)
    assert len(result) == len(matrix_a) and len(result[0]) == len(matrix_b[0]), "Result matrix dimension is invalid"

    return result


if __name__ == "__main__":
    print(*get_transpose([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
    print(*get_matrices_sum([(1, 2, 3), (9, 15, 76)], [(54, 23, 77), (4, 7, 2)]))
    print(*get_matrices_product([(1, 2, 3), (9, 15, 76)], [(54, 4, 1), (23, 7, 5), (77, 2, 6)]))
