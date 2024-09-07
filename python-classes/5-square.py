#!/usr/bin/python3
"""
task 5
"""


class Square:
    """
    # a square
    """
    def __init__(self, size=0):
        """
        init method
        :param size: the size of the square. Must be a non-negative integer
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the area of the square based on its size
        :return: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints the square using the '#' character
        """
        for i in range(self.__size):
            print("#" * self.__size)

    @property
    def size(self):
        """
        retrieves the size of the square
        :return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square
        :param value: the new size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
