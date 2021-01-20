#!/usr/bin/python3

"""This module defines a function "def class_to_json(obj)",
that reads a file and gets the dictionary of an object.

Usage:
    "def class_to_json(...)" receives an object "obj" and
    returns its dictionary.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple
    data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
        obj (object): class to retrieve its dictionary.

    Return:
        JSON string of dictionary.
    """
    return obj.__dict__
