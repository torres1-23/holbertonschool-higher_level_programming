#!/usr/bin/python3

"""This module defines an object dict return function.

Usage:
    "def lookup(obj)" is used to return a dictionary of methods
    of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.
    Args:
        obj (type): Object to return list of methods.

    Return:
        list of methods of object.
    """
    return(dir(obj))
