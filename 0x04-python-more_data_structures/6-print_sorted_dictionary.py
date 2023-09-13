#!/usr/bin/python3
# task 6-print_sorted_dictionary.py
def print_sorted_dictionary(a_dictionary):
    list_ord = list(a_dictionary.keys())
    list_ord.sort()
    for j in list_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
