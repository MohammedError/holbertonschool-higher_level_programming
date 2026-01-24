#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (integer or float).

    Returns:
        A new matrix with the result of the division, rounded to 2 decimal
        places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_row = 0

    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(msg_type)

        if i == 0:
            len_row = len(row)
        elif len(row) != len_row:
            raise TypeError(msg_size)

        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg_type)

    return [[round(item / div, 2) for item in row] for row in matrix]
