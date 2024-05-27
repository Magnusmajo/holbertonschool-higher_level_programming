class Square:
    """_
    A class definition for a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        _init_
        Main construction function for square

        Args:
            size (int, arg): Size for the square. Defaults to 0.
            position (tuple, arg): Position for the square. Defaults to (0, 0).
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

    @property
    def position(self):
        """
        position: It defines the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The value for the position function

        Raises:
            TypeError: Position not tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) is not 2 or not \
            all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        The area

        Returns:
            int: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print(" " * self.__size)
            for i in range(self.__size):
                print("#" * self.__size)
                