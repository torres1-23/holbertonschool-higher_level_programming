#!/usr/bin/python3

"""This module defines a function
"def add_attribute(o_class, attribute, value)".

Usage:
    "def add_attribute(...)" is used to add an attribute to an object if it is
    possible.
"""


def add_attribute(obj, att_name, value):
    """Sets attribute of a given a object if possible.

    Args:
        obj (object): Object to add an attribute.
        att_name (string): Name of new attribute.
        value (object): Valu of new attribute.

    Raises:
        TypeError: If attribute can't be added.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att_name, value)
