#!/usr/bin/python3
"""
BaseGeometry:
- public instance method called area.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square is a Rectangle with equal width and height.
    Arg:
    size (int): The size of the square.
    """


    def __init__(self, size):
        """
        Initialize a Square.
        Args:
            size (_type_): _description_
        """
        if self.integer_validator("size", size):
            self.__size = size

    def area(self):
        """
        Defines the area of the square
        Returns:
        int: The area of the square
        """
        return self.__size ** 2
