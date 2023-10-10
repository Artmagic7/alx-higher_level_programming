#!/usr/bin/python3
"""Clarifies a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a txt file using JSON representatn."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
