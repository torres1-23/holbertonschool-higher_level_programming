#!/usr/bin/python3

"""This module defines a class Square.

Usage:
    "class Square" inherits from "class Rectangle",
    creates new instance of Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inherits from class Rectangle."""

    def __init__(self, size):
        """Initializes instances of Square.

        Args:
            size (int): size of square instance.

        Attributes:
            __size (int): size of square instance.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
