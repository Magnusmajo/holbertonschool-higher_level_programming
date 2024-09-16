#!/usr/bin/python3
""""
Hello
"""


def print_square(size):
    """
    This function prints a square of a given size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
