#!/usr/bin/python3
"""Module that defines a class Rectangle"""


class Rectangle:
    """Class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the Square instance."""
        self.__height = height
        self.__width = width
        """The private width and height of the rectangle."""

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        Args:
            value (int): The width of the rectangle.
            Raises:
                TypeError: If width is not an integer.
                ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter
        If width or height is zero, returns 0"""
        if self.__width == 0 or self.__height:
            return 0
        return 2 * (self.__width + self.__height)
