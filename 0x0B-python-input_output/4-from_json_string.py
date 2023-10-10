#!/usr/bin/python3
# Task 4-from_json_string.py
"""Clarifies a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Retrn the Python object representation of a JSON string."""
    return json.loads(my_str)
