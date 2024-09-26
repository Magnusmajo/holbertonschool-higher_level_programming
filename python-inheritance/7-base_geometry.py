#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """An empty class named BaseGeometry"""
    pass

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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater then 0".format(name))
        else:
            return True
