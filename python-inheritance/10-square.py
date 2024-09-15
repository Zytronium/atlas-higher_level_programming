#!/usr/bin/python3
"""
    A module for basic shapes. This module
    demonstrates the concept of inheritance.
"""


class BaseGeometry:
    """a base shape"""
    def area(self):
        """
        raises an Exception if the subclass that calls it hasn't implemented
        its own area() method (or if a BaseGeometry class calls it)
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value
        :param name: the name, which is always a string
        :param value: the value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    a rectangle, which is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """
        calculates the area of the rectangle
        :return: the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
