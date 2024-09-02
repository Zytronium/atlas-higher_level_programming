#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0

    for item in my_list:
        if n < x:
            try:
                print(item, end='')
                n += 1
            except TypeError:
                break
    print()
    return n
