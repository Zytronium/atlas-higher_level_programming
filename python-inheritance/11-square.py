#!/usr/bin/python3
"""
    A module for basic shapes. This module
    demonstrates the concept of inheritance.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    a square, which is a subclass of Rectangle
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """
        calculates the area of the square
        :return: the area of the square
        """
        return self.__size * self.__size
