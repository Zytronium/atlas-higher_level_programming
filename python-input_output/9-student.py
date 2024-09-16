#!/usr/bin/python3
"""
module for task 9
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

    def to_json(self):
        """
        returns a json representation of itself
        :return: a json representation of this student
        """
        return self.__dict__
