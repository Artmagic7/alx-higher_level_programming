#!/usr/bin/python3
# task 2-replace_in_list.py


def replace_in_list(my_list, idx, element):
    """Replaces elemnt of a list at specific positn."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
