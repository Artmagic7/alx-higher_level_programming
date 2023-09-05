#!/usr/bin/python3
# task 100-print_tebahpla.py

""""Prints ASCII alphabet in reverse order alternating Lower and Upper case."""
j = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - j)), end="")
    j = 32 if j == 0 else 0
