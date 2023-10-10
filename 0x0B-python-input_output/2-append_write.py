#!/usr/bin/python3
"""Clarifies a file-appending function."""


def append_write(filename="", text=""):
    """Adjoins a string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to adjoin to.
        text (str): The string to adjoin to the file.
    Returns:
        The nmbr of characters adjoined.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
