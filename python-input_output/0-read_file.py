#!/usr/bin/python3
"""
module for task 0 which reads a file and prints its contents
"""
def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it
    :param filename: the name of file
    """
    f = open(filename)  # todo: handle exception?
    contents = f.read()  # todo: handle exception?
    print(contents)
    f.close()
