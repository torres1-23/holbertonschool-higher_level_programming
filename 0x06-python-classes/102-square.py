#!/usr/bin/python3

""" Define class Square. """


class Square:
    """Represents a square. """

    def __init__(self, size=0):
        """Initializes instance of square.

        Args:
            size (int): size of square.

        Attributes:
            size (method): sets a square size.
        """
        self.size = size

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

    def area(self):
        """Returns the current square area.

        Returns:
            Current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares are equal.

        Returns:
            True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares are not equal.

        Returns:
            True if not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if self square is greater than other.

        Returns:
            True if self square is greater than other, False otherwise.
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """Checks if self square is lesser than other.

        Returns:
            True is self square is lesser than other, False otherwise.
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """Checks if self square is greater or equal than other.

        Returns:
            True is self square is greater or equal than other,
            False otherwise.
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """Checks if self square is lesser or equal than other.

        Returns:
            True is self square is lesser or equal than other, False otherwise.
        """
        return self.area() <= other.area()
