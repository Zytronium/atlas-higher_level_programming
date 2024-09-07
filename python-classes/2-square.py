#!/usr/bin/python3
"""
# task 2
"""


class Square:
    """
    # a square
    """
    def __init__(self, size=0):
        """
        # init method
        :param size: the size of the square. Must be a non-negative integer
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
