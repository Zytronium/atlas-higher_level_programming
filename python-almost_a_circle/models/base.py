#!/usr/bin/python3
"""
module containing the base class for all objects in this project
"""


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