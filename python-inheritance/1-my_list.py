#!/usr/bin/python3
"""
    module for task 1
"""


class MyList(list):
    """
    the same thing as a list, but with a method to print itself sorted
    """
    def print_sorted(self):
        """
        prints the list, sorted in ascending order. Assumed all items are ints
        """
        print(sorted(self))
