#!/usr/bin/python3
"""This module defines a class "class Rectangle"."""
from models.base import Base


class Rectangle(Base):
    """This class defines instaces of rectangle, inherits from class "Base"."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of rectangle.

        Args:
            width (int): width of each instance.
            height (int): height of each instance.
            x (int, optional): attribute x of each instance,
            0 by default.
            y (int, optional): attribute y of each instance,
            0 by default.
            id (int, optional): id of each instance,
            None by default.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width attribute of each instance.

        Return:
            width of each instance.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute of each instance.

        Args:
            value (int): value to set.

        Attributes:
            width (int): width of each instance.

        Raises:
            TypeError: if value is not integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height attribute of each instance.

        Return:
            height of each instance.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute of each instance.

        Args:
            value (int): value to set.

        Attributes:
            height (int): height of each instance.

        Raises:
            TypeError: if value is not integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x attribute of each instance.

        Return:
            x of each instance.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x attribute of each instance.

        Args:
            value (int): value to set.

        Attributes:
            x (int): x of each instance.

        Raises:
            TypeError: if value is not integer.
            ValueError: if value is < 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y attribute of each instance.

        Return:
            y of each instance.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y attribute of each instance.

        Args:
            value (int): value to set.

        Attributes:
            y (int): y of each instance.

        Raises:
            TypeError: if value is not integer.
            ValueError: if value is < 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of rectangle.

        Return:
            Area of Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
        for i in range(self.y):
            print()
        for i in range(0, self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(0, self.width):
                print('#', end='')
            print()

    def __str__(self):
        """Computes string representation of each Rectangle instance.

        Return:
            String representation of each Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """Assigns an argument to each attribute."""
        cont = 0
        for arg in args:
            if cont == 0:
                self.id = arg
            if cont == 1:
                self.width = arg
            if cont == 2:
                self.height = arg
            if cont == 3:
                self.x = arg
            if cont == 4:
                self.y = arg
            cont += 1
