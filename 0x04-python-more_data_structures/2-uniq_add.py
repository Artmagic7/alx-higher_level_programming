#!/usr/bin/python3
# task 2-uniq_add.py
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    for j in uniq_list:
        num += j

    return (num)
