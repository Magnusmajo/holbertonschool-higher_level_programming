#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """An empty class named BaseGeometry"""

    def area(self):
        """Public instance method that Calculates the area of the Geometry.
        Raises:
            Exception: If the method has not been implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.
        Args:
            name (str): The name.
            value (int): The value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        else:
            return True
