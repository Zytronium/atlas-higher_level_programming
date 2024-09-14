#!/usr/bin/python3
"""
    task 4
"""


def inherits_from(obj, a_class):
    """
    checks if the given object inherits the given class directly or indirectly
    but is not the given class
    :param obj: the object to check if its the same class as the given class
    :param a_class: the class to check if its the same as the class of obj
    :return: True if the object inherits the given class but is not
    the given class
    """
    return isinstance(obj, a_class) if type(obj) is not a_class else False
