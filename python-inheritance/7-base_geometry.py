#!/usr/bin/python3
"""
    an empty class
"""


class BaseGeometry:
    """ an empty class"""
    def area(self):
        """
        raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        :param name: the name, which is always a string
        :param value: the value to be validated
        :return:
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
