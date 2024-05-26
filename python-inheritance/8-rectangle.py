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
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        
class Rectangle(BaseGeometry):
    """
    Rectangle class
    """


    def __init__(self, width, height):
        """
        Initializes Rectangle
        """
        self._width = width
        self._height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

