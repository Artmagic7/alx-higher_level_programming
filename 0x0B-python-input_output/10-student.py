#!/usr/bin/python3
"""Clarifies a class Student."""


class Student:
    """Represent a student."""

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

    def to_json(self, attrs=None):
        """Get a dictionary represntatn of the student.

        If attrs is a list of strings, represnts only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represnt.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
