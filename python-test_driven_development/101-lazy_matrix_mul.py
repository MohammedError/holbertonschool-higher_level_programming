#!/usr/bin/python3
"""
The 101-lazy_matrix_mul module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    return np.matmul(m_a, m_b)
