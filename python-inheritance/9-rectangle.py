#!/usr/bin/python3
"""
    a class
"""


class BaseGeometry:
    """a base class"""
    def area(self):
        """
        raises an Exception
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
    a rectangle
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
