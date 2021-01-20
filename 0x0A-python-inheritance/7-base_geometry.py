#!/usr/bin/python3

"""This module defines a class BaseGeometry.

Usage:
    "class BaseGeometry" defines methods thst computes geometry concepts.
"""


class BaseGeometry:
    """Represents a BaseGeometry."""

    def area(self):
        """Raises an exception.

        Raises:
            Exception: Always this method is called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates "value" argument as a positive integer.

        Args:
            name (string): name of the variable.
            value (int): value to check if it is a positive integer.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
