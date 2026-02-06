#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri_prev = tri[-1]
        tri_curr = [1]
        for i in range(len(tri_prev) - 1):
            tri_curr.append(tri_prev[i] + tri_prev[i + 1])
        tri_curr.append(1)
        tri.append(tri_curr)
    return tri
