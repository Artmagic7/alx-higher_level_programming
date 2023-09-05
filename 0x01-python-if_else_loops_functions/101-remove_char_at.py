#!/usr/bin/python3
# task 101-remove_char_at.py


def remove_char_at(str, n):
    """Clone a copy of the string take out charactr at positn n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
