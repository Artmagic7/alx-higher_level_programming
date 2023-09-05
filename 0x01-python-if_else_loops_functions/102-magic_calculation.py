#!/usr/bin/python3
# task 102-magic_calculation.py


def magic_calculation(a, b, c):
    """Write functn doing same as provided by Holberton School."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
