#!/usr/bin/python3
"""
module for task 6 which creates an Object based on a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a JSON file
    :param filename: the name of file to read from
    :return the object created from the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
