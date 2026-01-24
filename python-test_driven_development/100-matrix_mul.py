#!/usr/bin/python3
"""
This is the "100-matrix_mul" module.

The 100-matrix_mul module supplies one function, matrix_mul(m_a, m_b).
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a: The first matrix (list of lists of integers/floats).
        m_b: The second matrix (list of lists of integers/floats).

    Returns:
        The resulting matrix.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty.
        TypeError: If m_a or m_b contain non-integers/floats.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a and m_b cannot be multiplied.
    """
    # 1. Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    # 2. Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 3. Check if m_a is a list of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    # 4. Check if m_b is a list of lists
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # 5. Check if m_a is empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    # 6. Check if m_b is empty
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 7. Check elements of m_a
    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    # 8. Check elements of m_b
    for row in m_b:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 9. Check if m_a is rectangular
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise TypeError("each row of m_a must be of the same size")

    # 10. Check if m_b is rectangular
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise TypeError("each row of m_b must be of the same size")

    # 11. Check multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform Multiplication
    # Result dimensions: rows_a x cols_b
    res = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            new_row.append(sum_val)
        res.append(new_row)

    return res
