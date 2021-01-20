#!/usr/bin/python3

"""This module defines a class Rectangle.

Usage:
    "class Rectangle" inherits from class BaseGeometry,
    creates new instance of Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from class BaseGeometry."""
    def __init__(self, width, height):
        """Initializes instances of Rectangle.

        Args:
            width (int): width of rectangle instance.
            height (int): height of rectangle istance.

        Attributes:
            __width (int): width of rectangle instance.
            __height (int): height of rectangle instance.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Computes area of a rectangle.

        Return:
            Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Computes a string representation of the instance.

        Return:
            String representation of a rectangle instance.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
