#!/usr/bin/python3
"""
    This module, from task 0, contains a function that adds 2 integers.
"""


def add_integer(a, b=98):  # normally we would probably rather do b=0
    """
    Adds integers a and b and returns the result
    :param a: first integer
    :param b: second integer. B = 98 if not specified
    :return: the sum of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
