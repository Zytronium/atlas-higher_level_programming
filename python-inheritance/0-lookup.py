#!/usr/bin/python3
"""
    module for task 0
"""


def lookup(obj) -> list:
    """
    returns the list of available attributes and methods of an object
    :param obj: the object to look up
    :return: a list of available attributes and methods of the object
    """
    return dir(obj)
