#!/usr/bin/python3
# task 11-delete_at.py


def delete_at(my_list=[], idx=0):
    """Deletes item at specific positn in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
