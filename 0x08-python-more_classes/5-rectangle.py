#!/usr/bin/python3

"""This module defines a class Rectangle.

Usage:
    Class Rectangle is used to instanciate rectangles.
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

    def area(self):
        """ Computes the current rectangle area.

        Returns:
            Current rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """ Computes the current rectangle perimeter.

        Returns:
            Current rectangle perimeter or 0 if height or width = 0.
        """
        if self.width is 0 or self.height is 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def __str__(self):
        """Defines the printable representation of a rectangle.

        Returns:
            String representation of a rectangle using "#" character.
        """
        string = ""
        if self.width != 0 and self.height != 0:
            for i in range(self.height - 1):
                for j in range(self.width):
                    string += "#"
                string += "\n"
            for j in range(self.width):
                string += "#"
        return string

    def __repr__(self):
        """Defines a string representation of a rectangle.

        Returns:
            String representation of a rectangle instance.
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Deletes a rectangle instance and print a message"""
        print("Bye rectangle...")
