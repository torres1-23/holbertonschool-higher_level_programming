#!/usr/bin/python3

"""This module defines class that inherits from list.

Usage:
    "class MyList(list)" is used to add new methods to the list class,
    from which it inherates.
"""


class MyList(list):
    """Class that inherites from list to add new methods to that class."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
