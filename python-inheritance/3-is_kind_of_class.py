#!/usr/bin/python3
"""
    a function for task 3
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of the specified class
    or a subclass of it; otherwise False
    :param obj: the object to check if its the same class as the given class
    :param a_class: the class to check if its the same as the class of obj
    :return: True if the object is exactly an instance of the specified class
    or a subclass of it; otherwise False
    """
    return isinstance(obj, a_class)
