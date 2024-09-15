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
