#!/usr/bin/python3

"""This module defines a function that checks if an object is exactly
   an instance of a class.

Usage:
    "def is_same_class(obj, a_class)" is used to check if the argument "obj"
    is exactly an instance of the argument "a_class".
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class.

    Args:
        obj (any): instance to check.
        a_class (class): class to check if obj is instance of.

    Return:
        True: if the object is exactly an instance of the class.
        False: Otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
