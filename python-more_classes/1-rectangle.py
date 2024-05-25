#!/usr/bin/python3
"""
Rectangle: 
Defines a Rectangle class
"""

class Rectangle:
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        
        Keyword arguments:
        value -- the value of the width, must be an integer >= 0
        Raise:
        TypeError exception if not an integer
        ValueError exception if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        
        Keyword arguments:
        value -- the value of the height, must be an integer >= 0
        Raise:
        TypeError exception if not an integer
        ValueError exception if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value