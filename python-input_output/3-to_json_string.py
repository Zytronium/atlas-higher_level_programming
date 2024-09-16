#!/usr/bin/python3
"""
module for task 3 which converts an object into a json string
"""
import json


def to_json_string(my_obj):
    """
    converts an object to a json string
    :param my_obj: the object to convert to a json string
    :return: the object as json string
    """
    return json.dumps(my_obj)
