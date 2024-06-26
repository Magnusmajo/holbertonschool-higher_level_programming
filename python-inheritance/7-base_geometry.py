#!/usr/bin/python3
"""
BaseGeometry:
- public instance method called area.
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Raises a NotImplementedError
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        else:
            return True
