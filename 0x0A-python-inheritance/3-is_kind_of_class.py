#!/usr/bin/python3

"""This module defines a function that checks if an object is an
   instance of a class or a class that inherited from.

Usage:
    "def is_kind_of_class(obj, a_class)" is used to check if the argument "obj"
    is an instance of the argument "a_class" or from a clas that inherited
    from.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or
       a subclass that inherited from.

    Args:
        obj (any): instance to check.
        a_class (class): class to check if obj is instance of,
        or instance of a subclass that inherited from.

    Return:
        True: if the object is an instance of the class or
        instance of a subclass that inherited from..
        False: Otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
