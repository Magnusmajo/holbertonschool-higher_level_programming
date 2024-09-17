#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """A class named Square that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance.
        Args:
            size (int): The size of the square initialized in zero.
            position (tuple): The position of the square initialized in (0, 0).
        """
        self.__size = size
        self.position = position

    def area(self):
        """Public instance method that Calculates the area of the square.
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the square.
        Args:
            size (int): The size of the square.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the position of the square.
        Args:
            position (tuple): The position of the square.
            Raises:
                TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """Public instance method that
        prints in stdout the square
        with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for t in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
