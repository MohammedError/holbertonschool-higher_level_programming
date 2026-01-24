#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer(a, b=98).
"""


def add_integer(a, b=98):
    """
    Return the addition of two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
