#!/usr/bin/python3
"""
module for task 4 which converts a
python data structure object into a json string
"""
import json


def from_json_string(my_str):
    """
    converts a JSON string representing a Python data structure to that object
    :param my_str: the string to convert to an object
    :return: the object (Python data structure) represented by the JSON string
    """
    return json.loads(my_str)
