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
        Arg:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
