#!/usr/bin/python3

"""This module defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a BaseGeometry."""
    def area(self):
        """Raises an exception.

        Raises:
            Exception: Always this method is called.
        """
        raise Exception("area() is not implemented")
