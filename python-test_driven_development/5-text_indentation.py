#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The string to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            print(result.strip())
            print()
            result = ""

    if result.strip():
        print(result.strip(), end="")
