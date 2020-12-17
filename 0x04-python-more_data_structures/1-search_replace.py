#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list. """
    newlist = my_list[:]
    return [replace if n == search else n for n in newlist]
