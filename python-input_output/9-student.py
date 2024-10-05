#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """the given instantiation for student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student class to JSON
        Args:
            attrs: list of attributes
        Returns:
            dict: dictionary representation of a simple data structure
        """
        return self.__dict__
