#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.

The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul(m_a, m_b).
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.
    """
    return np.matmul(m_a, m_b)
