#!/usr/bin/python3
# task 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Prints all integrs of a list in reverse ordr."""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
