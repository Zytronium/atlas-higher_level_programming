#!/usr/bin/python3
"""
module containing the base class for all objects in this project
"""
import json


class Base:
    """
    The base of all other classes in this project.
    The goal of it is to manage id attribute in all future classes, and
    to avoid duplicating the same code (by extension, the same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
        gets the list of the JSON string representation json_string
        (reverse of to_json_string)
        :param json_string: a json string representation of a list of objects
        :return: a list of dictionaries which the given json string represents
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        gets the JSON string representation of a list of dictionaries.
        :return: the JSON string representation of the
        given list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        :param list_objs: list of instances, which inherit the Base class,
        which will be written to a file
        """
        class_name = cls.__name__
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        with open(f"{class_name}.json", "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        creates & returns an instance with all attributes already set
        :param dictionary: a dictionary representing an object of cls
        :return: an instance of cls with all attrs set from dictionary
        """


if __name__ == '__main__':
    b = Base()
    print(b.id)
    b2 = Base()
    print(b2.id)
    b2.id = 3
    print(b2.id)
    b3 = Base()
    print(b3.id)
    b4 = Base(12)
    print(b4.id)
