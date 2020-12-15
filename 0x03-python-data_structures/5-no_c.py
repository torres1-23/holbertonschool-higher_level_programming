#!/usr/bin/python3
def no_c(my_string):
    """ Removes all characters c and C from a string. """
    copy_string = ""
    for n in range(len(my_string)):
        if my_string[n] != "c" and my_string[n] != "C":
            copy_string += my_string[n]
    return(copy_string)
