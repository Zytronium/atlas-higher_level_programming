#!/usr/bin/python3
"""
module for task 11
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

    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student instance:
        :param json: the dict to load from
        """
        for item in json:
            self.__dict__[item] = json[item]
