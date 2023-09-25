#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elemnts of list.
    Args:
    my_list (list): The list to print elemnts from.
    x (int): The nmbr of elemnts of my_list to print.

    Returns:The nmbr of elemnts printed.
    """
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ret += 1
        except IndexError:
            break
        print("")
        return (ret)
