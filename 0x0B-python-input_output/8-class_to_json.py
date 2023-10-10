#!/usr/bin/python3
"""Clarifies a Python class-to-JSON function."""


def class_to_json(obj):
    """Retrn the dictionary represntatn of a simple data structure."""
    return obj.__dict__
