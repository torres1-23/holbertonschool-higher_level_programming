#!/usr/bin/python3

"""This module defines a print function
   "def say_my_name(first_name, last_name="")"
   that prints "My name is <first name> <last name>".

Usage:
    "def say_my_name(...)" must receive valid strings,
    prints "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """Prints a name in a given format.

    Args:
        first_name (str): first name.
        last_name (str, optional): last name.

    Raises:
        TypeError: if first_name is not a string.
        TypeError: if last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
