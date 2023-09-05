#!/usr/bin/python3
# task 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for i in range(10):
    for j in range(i + 1, 10):
        if i != j:
            print("{:d}{:d}".format(i, j), end=", " if i < 8 else "\n")
