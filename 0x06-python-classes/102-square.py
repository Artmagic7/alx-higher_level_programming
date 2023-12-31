#!/usr/bin/python3
"""To define a class Square."""

class Square:
    """Reprsnt a square."""

    def __init__(self, size=0):
        """Initialises a new square.

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set recent size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return recent area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defines the == comparisn to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparisn to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparisn to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparisn to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparisn to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarisn to a Square."""
        return self.area() >= other.area()
