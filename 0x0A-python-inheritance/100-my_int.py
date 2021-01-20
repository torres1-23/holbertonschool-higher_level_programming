#!/usr/bin/python3

""" Define class MyInt.
Usage:
    "class MyInt" inherits from class int,
    used for adding methods to class int"""


class MyInt(int):
    """Represents a MyInt instance, inherits from class int.
    Methods to check equality are inverted according to the requirements.
    """
    def __eq__(self, other):
        """Checks if two integers are not equal.

        Returns:
            True if not equal, False otherwise.
        """
        return int(self) != other

    def __ne__(self, other):
        """Checks if two integers are equal.

        Returns:
            True if equal, False otherwise.
        """
        return int(self) == other
