#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    num1a = tuple_a[0] if len(tuple_a) > 0 else 0
    num2a = tuple_a[1] if len(tuple_a) > 1 else 0
    num1b = tuple_b[0] if len(tuple_b) > 0 else 0
    num2b = tuple_b[1] if len(tuple_b) > 1 else 0

    return (num1a + num1b), (num2a + num2b)
