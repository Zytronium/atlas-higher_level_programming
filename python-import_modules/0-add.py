#!/usr/bin/python3
add = __import__('add_0').add
a = 1
b = 2
print("{a} + {b} = {c}".format(a = a, b = b, c = add(a, b)))