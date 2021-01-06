#!/usr/bin/python3

"""Creates a sorted songle linked list."""


class Node:
    """Represents a node for a single linked list."""

    def __init__(self, data, next_node=None):
        """Initializes instance of a node.

        Args:

            data (int): data of each node.
            next_node (Node): next node of new node.

        Attributes:

            data (method): sets the node data.
            next_node (method): sets the next node to point.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the node data.

        Returns:

            Current node data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets a square size.

        Args:

            value (int): node data.

        Attributes:

            __data (int): node data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node of current node.

        Returns:

            Next node of current node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node of the current node.

        Args:

            value (Node): next node of current node.

        Attributes:

            __next_node (Node): next node of current node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Represents a single linked list."""

    def __init__(self):
        """Initializes a single linked list.

        Attributes:

            __head (Node): head node of single linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the single linked list in ascending order.

        Args:

            value (int): value of the new node
        """
        new = Node(value)
        if not self.__head:
            new.next_node = None
            self.__head = new
        elif value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and value > tmp.next_node.data:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print representation of the single linked list.

        Returns:

            String containing each data of each node of the single linked list:
        """
        tmp = self.__head
        string = ""
        if tmp:
            while tmp.next_node:
                string += str(tmp.data) + '\n'
                tmp = tmp.next_node
            string += str(tmp.data)
        return string
