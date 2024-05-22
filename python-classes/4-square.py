#!/usr/bin/python3
"""
Square:
A class that defines a square
"""

class Square:
    """_init_
    main construction function for square
    """
    def __init__(self, size=0):
        """
        Args:
            size (int, optional): Size for the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        size: It defines the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The value for the size function

        Raises:
            TypeError: Size not int
            ValueError: Size < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area

        Returns:
            int: Area of square
        """
        return self.__size ** 2