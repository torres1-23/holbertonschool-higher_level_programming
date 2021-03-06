#!/usr/bin/python3
"""This module defines a class "class Rectangle"."""
from models.base import Base
keys = ['id', 'width', 'height', 'x', 'y']


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
        for i in range(1, len(keys)):
            exec('self.{} = {}'.format(keys[i], keys[i]))

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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute or
        a key/value argument to attributes.

        Args:
            args (tuple): arguments to update.
            kwargs (dictionary): key/value pairs to update.
        """
        if args and len(args) > 0:
            i = 0
            for arg in args:
                if i is 0 and arg is None:
                    continue
                else:
                    try:
                        exec('self.{} = arg'.format(keys[i]))
                        i += 1
                    except IndexError:
                        break
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in keys:
                    if key == 'id' and value is None:
                        continue
                    else:
                        exec('self.{} = {}'.format(key, value))

    def to_dictionary(self):
        """Creates dictionary representation of Rectangle.

        Return:
            dictionary with each attribute of rectangle instance.
        """
        dic = {}
        for key in keys:
            exec('dic[key] = self.{}'.format(key))
        return dic
