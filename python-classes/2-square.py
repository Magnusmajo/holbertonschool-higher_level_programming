#!/usr/bin/python3

clas Square:
    def __init__(self, side=0):
        """
        Square:
        This is a constructor method

        Args:
            side (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(size, int):
        """_summary_

        Args:
            int (_type_): _description_

        Raises:
            TypeError: _description_
        """
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
