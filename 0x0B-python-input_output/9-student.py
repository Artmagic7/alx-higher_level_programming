#!/usr/bin/python3
"""Clarifies a class Student."""


class Student:
    """Represnt a student."""

    def __init__(self, first_name, last_name, age):
        """Initialise a new Student.

        Args:
            first_name (str): 1st name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary represntatn of student."""
        return self.__dict__
