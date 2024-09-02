#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_items = set()
    for item in set_1:
        if item not in set_2:
            unique_items.add(item)
    for item in set_2:
        if item not in set_1:
            unique_items.add(item)
    return unique_items
