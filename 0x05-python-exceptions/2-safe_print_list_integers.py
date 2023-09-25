#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints 1st x elemnts of  list that are integrs.

    Args:
        my_list (list): List to print elemnts from.
        x (int): Nmbr of elements of my_list to print.

    Returns: Nmber of elemnts printed.
    """
    ret = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
