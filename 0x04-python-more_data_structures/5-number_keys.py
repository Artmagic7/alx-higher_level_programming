#!/usr/bin/python3
# task 5-number_keys.py
def number_keys(a_dictionary):
    num = 0
    list_keys = list(a_dictionary.keys())

    for j in list_keys:
        num += 1

    return (num)
