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
    def load_from_file(cls):
        """
        creates a list of instances from a json file
        :return: a list of instances from a json file, which inherit Base
        """
        # get the list of dicts from the file
        file_name = cls.__name__ + ".json"
        list_objs = []
        try:
            with open(file_name, "r") as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        # turn the list of dicts into a list of instances
        for dictionary in list_dicts:
            list_objs.append(cls.create(**dictionary))
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """
        creates & returns an instance with all attributes already set.
        Basically the inverse of to_dictionary().
        :param dictionary: a dictionary representing an object of cls
        :return: an instance of cls with all attrs set from dictionary
        """
        if cls.__name__ == "Rectangle":  # Rectangle
            instance = cls(1, 1)  # width = 1, height = 1
        else:  # Square (or Base, but it has no update() method)
            instance = cls(1)  # size = 1 (square) or id = 1 (base)
        # Note: used cls.name to avoid importing, which causes circular import
        instance.update(**dictionary)
        return instance
