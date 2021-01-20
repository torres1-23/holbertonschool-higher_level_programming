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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigth", height)
        self.__height = height
