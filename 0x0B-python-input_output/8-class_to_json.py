#!/usr/bin/python3

"""This module defines a function "def class_to_json(obj)",
that reads a file and gets a JSON string.

Usage:
    "def class_to_json(...)" receives an object "obj" and
    returns its dictionary as a JSON string.
"""
import json


def class_to_json(obj):
    """Returns the dictionary description with simple
    data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
        obj (object): class to retrieve its dictionary.

    Return:
        JSON string of dictionary.
    """
    return json.dumps(obj.__dict__)
