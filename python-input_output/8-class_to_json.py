#!/usr/bin/python3
"""
module for task 8
"""
import json


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object, whatever that means...
    :param obj: an instance of a class
    :return: the dictionary description with simple data structure
    for JSON serialization of an object
    """
    return json.dumps(obj)
