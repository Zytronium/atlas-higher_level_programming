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

    def __del__(self):
        Base.__nb_objects -= 1

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
