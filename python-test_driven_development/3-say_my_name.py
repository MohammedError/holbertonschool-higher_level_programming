#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

The 3-say_my_name module supplies one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Args:
        first_name: The first name string.
        last_name: The last name string.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
