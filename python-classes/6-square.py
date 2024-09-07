#!/usr/bin/python3
"""
task 6
"""


class Square:
    """
    a square
    its dimensions are size*size characters
    when position is (x, y), the square is printed offset by x characters
    to the right, and y characters down.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        init method
        :param size: the size of the square. Must be a non-negative integer
        :param position: the (x, y) position of the square. Must be a tuple of
        2 positive integers.
        """
        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        if (type(position) is not tuple or len(position) != 2
                or type(position[0]) is not int or type(position[1]) is not int
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

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
        print("\n" * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        if self.__size == 0:
            print()  # still print something if size is 0

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

    @property
    def position(self):
        """
        retrieves the position of the square
        :return: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the new position of the square
        :param value: the new position of the square
        """
        if (type(value) is not tuple or len(value) != 2
            or type(value[0]) is not int or type(value[1]) is not int
            or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
