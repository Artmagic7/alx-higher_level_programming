#!/usr/bin/python3
"""Prints alphabet in uppercase then a new line"""
print(*list(map(chr, range(65, 91))), sep='')
