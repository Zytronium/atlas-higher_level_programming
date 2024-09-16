#!/usr/bin/python3
"""
module for task 2 which appends text to a file
"""


def append_write(filename="", text=""):
    """
    appends a string to the end of a text file (UTF8)
    :param filename: the name of file
    :return the number of characters written
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
