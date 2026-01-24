#!/usr/bin/python3
"""
Lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""

    # let NumPy handle non-list cases
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        try:
            return np.matmul(m_a, m_b)
        except Exception as e:
            print(e)
            return

    # empty checks
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # numeric values
    if not all(isinstance(x, (int, float)) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")

    # same row sizes
    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # multiplication rule
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
