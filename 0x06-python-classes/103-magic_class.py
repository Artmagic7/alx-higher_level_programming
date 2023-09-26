#!/usr/bin/python3
"""Define a MagicClass doing exactly a bytecode provided by ALX."""

import math


class MagicClass:
    """Repping a circle."""

    def __init__(self, radius=0):
        """Initialise a MagicClass.

        Arg:
            radius (float or int): Radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a nmbr")
        self.__radius = radius

    def area(self):
        """Retrn area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Retrn circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
