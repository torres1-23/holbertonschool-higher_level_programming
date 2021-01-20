#!/usr/bin/python3

"""This module defines a function "def to_json_string(my_obj)",
that converts a Python object into a JSON.

Usage:
    "def to_json_string(...)" converts a python object into a JSON.
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: (object): Python object to convert to JSON.

    Return:
        JSON representation of an object.
    """
    return json.dumps(my_obj)
