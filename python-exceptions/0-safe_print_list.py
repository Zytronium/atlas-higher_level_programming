#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    for item in my_list:
        if i < x:
            try:
                print(item, end='')
                i += 1
            except TypeError:
                break
    print()
    return i
