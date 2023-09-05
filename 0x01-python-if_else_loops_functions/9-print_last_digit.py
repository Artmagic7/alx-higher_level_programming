#!/usr/bin/python3
# task 9-print_last_digit.py


def print_last_digit(number):
"""Prints last digit of a nmbr and retrn it."""
 number = abs(number)

last_digit = number % 10
print(last_digit)
return last_digit

if __name__ == "__main__":

    number = int(input("Enter a number: "))
    last_digit = print_last_digit(number)
