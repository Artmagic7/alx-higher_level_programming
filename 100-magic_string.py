#!/usr/bin/python3
# Task 100-magic_string.py
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")

