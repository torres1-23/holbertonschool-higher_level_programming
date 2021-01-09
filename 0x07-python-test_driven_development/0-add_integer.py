#!/usr/bin/python3

"""This module defines an integer addition function "add_integer(a, b=98)"

Usage:
    "add_integer(...)" return the addition of two arguments,
    equivalent to using the "+" operator in numbers.
"""


def add_integer(a, b=98):
    """Function that adds 2 integers.

    Args:
        a (int): first number to add.
        b (int, optional): second number to add.

    Raises:
        TypeError: if a is not integer nor float.
        TypeError: if b is not integer nor float.

    Returns:
        int: Addition of the two integers.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
