#!/usr/bin/python3
""" Locates a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]

# Complexity: O(nlog(n))
