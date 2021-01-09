#!/usr/bin/python3

"""This module defines a print function
   "def print_square(size)"
   that prints a square using the "#" character".

Usage:
    "print_square(...)" must receive a valid integer "size,
    prints the square using the "#" character.
"""


def print_square(size):
    """ Prints a square.
    Args:
        size (int): size of the square.

    Raises:
        TypeError: if "size" is not an integer.
        ValueError: of "size" is lesser than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
