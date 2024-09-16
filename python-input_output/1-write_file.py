#!/usr/bin/python3
"""
module for task 1 which writes to a file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    :param filename: the name of file
    :return the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
