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

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)


