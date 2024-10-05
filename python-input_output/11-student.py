#!/usr/bin/python3
"""Student to JSON"""


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
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value
                    in self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        """Student class to JSON
        Args:
            json: dictionary representation of a simple data structure
        """
        for key, value in json.items():
            setattr(self, key, value)
