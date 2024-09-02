#!/usr/bin/python3
from traceback import TracebackException


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    i = 0

    for item in my_list:
        if i < x:
            try:
                print("{:d}".format(item), end='')
                n += 1
            except IndexError:
                print("Index Error")
            except ValueError:
                pass
            except TypeError:
                pass
            i += 1
    print()
    return i

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 3)
print("nb_print: {:d}".format(nb_print))