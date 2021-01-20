#!/usr/bin/python3

"""This module defines a function "def from_json_string(my_str)",
that converts a JSON string to a Python object.

Usage:
    "def from_json_string(...)" converts a JSON string into a Python object.
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string:

    Args:
        my_str: (str): JSON string.

    Return:
        Python object.
    """
    return json.loads(my_str)
