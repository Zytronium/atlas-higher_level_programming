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

if not issubclass(Rectangle, BaseGeometry):
    print(f"{Rectangle.__name__} is a subclass of {Rectangle.__bases__[0].__name__}")