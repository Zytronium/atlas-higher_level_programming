#!/usr/bin/python3
"""
    This module, from task 3, contains a function that prints a square
    with the character '#'.
"""


def print_square(size):
    """
    prints a square with the '#' character
    :param size: size of the square in characters (size x size)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
