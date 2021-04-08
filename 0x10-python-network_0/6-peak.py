#!/usr/bin/python3
"""This module defines a function that finds a peak in a list of unsorted
integers.
Usage:
    "find_peak" requires a list of unsorted integers and returns a peak.
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List in which to find a peak.
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
