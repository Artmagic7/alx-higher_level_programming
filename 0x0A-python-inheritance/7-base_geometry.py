#!/usr/bin/python3
"""Clarifies a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet enacted."""
        raise Exception("area() is not enacted")

    def integer_validator(self, name, value):
        """Verify a parameter as an integer.

        Args:
            name (str): Name of the parameter.
            value (int): Parameter to verify.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
