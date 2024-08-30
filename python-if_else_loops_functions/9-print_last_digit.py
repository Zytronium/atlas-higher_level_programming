#!/usr/bin/python3
def print_last_digit(number):
    print("{n}".format(n = int(str(number)[-1:])), end='')


print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)