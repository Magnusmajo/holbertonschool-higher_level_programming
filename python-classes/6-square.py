#!/usr/bin/python3
"""
Square:
    Defines a Square
"""


class Square:
    """
        Defines a Square
    """ 

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square
        Args:
        size (int): The size of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter for size
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        Getter for position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Setter for position
        Args:
        position (tuple): The position of the square
        """
        if not isinstance(position, tuple) or len(position) != 2 \
            or not isinstance(position[0], int) \
                or not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """
        Prints the square
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
            for i in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
