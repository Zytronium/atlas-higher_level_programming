#!/usr/bin/python3
"""
module for task 10
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a json representation of itself, with only the given
        attributes, or all attributes if none specified
        :param attrs: list of attributes (str keys)
        :return: a json representation of this student
        """
        json_dict = {}
        i = 0
        if type(attrs) is list:
            for attr in attrs:
                if self.__dict__.get(attr) is not None:
                    json_dict[attr] = self.__dict__[attr]
                    i += 1
            return json_dict
        return self.__dict__
