#!/usr/bin/python3

"""This module defines a function that checks if an object is an
   instance of a class that inherited from an specified class.

Usage:
    "def inherits_from(obj, a_class)" is used to check if the argument "obj"
    is an instance of a class that inherited from the argument "a_class"
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited from a specified class.

    Args:
        obj (any): instance to check.
        a_class (class): class to check if obj is instance of a
        subclass that inherited from.

    Return:
        True: if the object is an instance of a subclass that
        inherited from "a_class".
        False: Otherwise.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
