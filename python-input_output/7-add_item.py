#!/usr/bin/python3
"""
module for task 7
"""
from sys import argv
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json').load_from_json_file


if __name__ == '__main__':
    file_name = "add_item.json"
    try:
        my_list = load_json(file_name)
    except FileNotFoundError:
        my_list = []
    if len(argv) != 0:
        for item in argv:
            my_list.append(item)
        save_json(my_list, file_name)
