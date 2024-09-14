#!/usr/bin/python3
"""
    a function for task 2 that specifies whether an object's class is the
    given class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False
    :param obj: the object to check if its the same class as the given class
    :param a_class: the class to check if its the same as the class of obj
    :return: True if the object is exactly an instance of the specified class;
    otherwise False
    """
    return True if type(obj) is a_class else False
