#!/usr/bin/python3
# task 5-no_c.py


def no_c(my_string):
    """Remvs all charactrs c and C frm a string."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
