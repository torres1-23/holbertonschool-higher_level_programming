#!/usr/bin/python3

"""This module defines a function "def read_file(filename="")",
that reads a file.

Usage:
    "def read_file(...)" reads a file and print all its
    contents to the standard output.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): name of the file to read,
        empty string by default.
    """
    with open(filename, encoding="UTF8") as s_file:
        print(s_file.read(), end="")
