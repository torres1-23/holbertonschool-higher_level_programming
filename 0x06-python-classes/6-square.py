#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes instance of square.
        Args:
            size (int): size of square.
            position (tuple): position of square.
        Attributes:
            size (method): sets a square size.
            posiition (method): sets a square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets a square size.
        Returns:
            Current size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a square size.
        Args:
            value (int): size of square.
        Attributes:
            __size (int): size of square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets a square position.
        Returns:
            Tuple of square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets a square position.
        Args:
            value (tuple): position of current square.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area.
        Returns:
            Current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the current square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
