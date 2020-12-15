#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Prints all integers of a list, in reverse order. """
    my_list.reverse()
    [print("{:d}".format(n)) for n in my_list]
