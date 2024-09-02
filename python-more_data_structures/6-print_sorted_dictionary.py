#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{k}: {v}".format(k=key, v=value))
