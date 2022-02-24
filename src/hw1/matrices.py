def validate_matrix(matrix):
    if type(matrix) not in [list, tuple]:
        raise TypeError("Matrix must be list or tuple")
    for row in matrix:
        if type(row) not in [list, tuple]:
            raise TypeError("Row must be list or tuple")
    if len({len(row) for row in matrix}) > 1:
        raise IndexError("Rows dimensions are not equal")

    return True


def get_transpose(matrix):
    if validate_matrix(matrix):
        transposed_matrix = list(zip(*matrix))
        assert validate_matrix(transposed_matrix), "Result is not a matrix"
        assert len(transposed_matrix) == len(matrix[0]) and len(transposed_matrix[0]) == len(
            matrix
        ), "Result matrix dimension is invalid"
        return transposed_matrix
    else:
        raise TypeError("Matrix is invalid")


def get_matrices_sum(matrix_a, matrix_b):
    if validate_matrix(matrix_a) and validate_matrix(matrix_b):
        if len(matrix_a) == len(matrix_b) and len(matrix_a[0]) == len(matrix_b[0]):
            try:
                result = [tuple(x + y for (x, y) in zip(row_a, row_b)) for row_a, row_b in zip(matrix_a, matrix_b)]
            except TypeError as error:
                raise TypeError("Values inside could not be multiplied") from error

            assert validate_matrix(result), "Result is not a matrix"
            assert len(result) == len(matrix_a) and len(result[0]) == len(
                matrix_a[0]
            ), "Result matrix dimension is invalid"
            return result
        else:
            raise IndexError("Matrices dimensions are not equal")
    else:
        raise TypeError("One of matrices is invalid")


def get_matrices_product(matrix_a, matrix_b):
    if validate_matrix(matrix_a) and validate_matrix(matrix_b):
        transposed_matrix_b = get_transpose(matrix_b)
        assert validate_matrix(transposed_matrix_b)
        try:
            result = [
                tuple(sum(x * y for (x, y) in zip(row_a, row_b)) for row_b in transposed_matrix_b) for row_a in matrix_a
            ]
        except TypeError as error:
            raise TypeError("Values inside could not be multiplied") from error

        assert validate_matrix(result), "Result is not a matrix"
        assert len(result) == len(matrix_a) and len(result[0]) == len(matrix_b[0]), "Result matrix dimension is invalid"
        return result


if __name__ == "__main__":
    print(*get_transpose([(1, 2, 3), (4, 5, 6)]))
    print(*get_matrices_sum([(1, 2, 3), (9, 15, 76)], [(54, 23, 77), (4, 7, 2)]))
    print(*get_matrices_product([(1, 2, 3), (9, 15, 76)], [(54, 4, 1), (23, 7, 5), (77, 2, 6)]))
