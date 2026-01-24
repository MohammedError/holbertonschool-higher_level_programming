#!/usr/bin/python3
"""
This module provides a function that multiplies two matrices
using the NumPy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        The result of the matrix multiplication.
    """
    return np.matmul(m_a, m_b)
