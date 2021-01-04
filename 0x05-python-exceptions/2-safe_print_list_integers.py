#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    """ Prints the first x elements of a list and only integers.
    Args:
        my_list (list): A list with any type of items.
        x (int): number of items to acces in list.
    Returns:
        real number of integers printed.
    """

    cont = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cont += 1
        except (TypeError, ValueError):
            continue
    print()
    return cont
