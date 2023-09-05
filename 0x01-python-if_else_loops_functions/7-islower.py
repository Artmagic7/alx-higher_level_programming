#!/usr/bin/python3
# task 7-islower.py


def islower(c):
    """Checking for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
