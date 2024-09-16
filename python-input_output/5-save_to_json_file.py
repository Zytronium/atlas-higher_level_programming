#!/usr/bin/python3
"""
module for task 5 which writes an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    :param my_obj: the object to write to the file
    :param filename: the name of file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
