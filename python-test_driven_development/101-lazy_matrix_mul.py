#!/usr/bin/python3
"""
Module to multiply 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module
    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        return m_a * m_b
    """
    return np.matmul(m_a, m_b)
