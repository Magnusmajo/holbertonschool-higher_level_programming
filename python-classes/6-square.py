##!/usr/bin/python3
"""
Square:
    A class that defines a square
"""


class Square:
    """
    A class definition
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        _init_
        main construction function for square
        Args:
            size (int, arg): Size for the square.
            Defaults to 0.
            position (tuple, arg): Position of the square.
            Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area
        Returns:
            int: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square"""

        if (self.__size == 0):
            print()
            return

        [print() for a in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end='') for j in range(self.__position[0])]
            [print("#", end='') for k in range(self.__size)]
            print()
