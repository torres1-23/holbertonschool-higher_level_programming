#!/usr/bin/python3

"""This module defines an empty class Rectangle.

Usage:
    Class Rectangle is used to instanciate empty rectangles.
"""


class Rectangle:
    """Represent an empty rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes instance of rectangle.

        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets the current rectangle width.

        Returns:
            Current rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle.

        Args:
            value (int): width of rectangle.

        Attributes:
            __width (int): width of new instance of rectangle.

        Raises:
            TypeError: if value is not int.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the current rectangle height.

        Returns:
            Current rectangle heigth.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle.

        Args:
            value (int): height of rectangle.

        Attributes:
            __height (int): height of new instance of rectangle.

        Raises:
            TypeError: if value is not int.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
