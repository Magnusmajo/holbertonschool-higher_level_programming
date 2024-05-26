#!/usr/bin/python3
"""
BaseGeometry:
- public instance method called area.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """
        Implements area() for Rectangle
        """
        return self._width * self._height

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        """
        return f"[Rectangle] {self._width}/{self._height}"
