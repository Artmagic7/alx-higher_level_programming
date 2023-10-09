#!/usr/bin/python3
"""Clarifies an object attribute lookup function."""


def lookup(obj):
    """Retrns a list of an object's available attributes."""
    return (dir(obj))
