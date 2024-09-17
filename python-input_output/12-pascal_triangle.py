#!/usr/bin/python3
"""
    module for task 12
"""


def pascal_triangle(n: int):
    """
    creates a matrix of ints representing the Pascal’s triangle of n
    :param n: number of rows to generate
    :return: a list of lists of ints representing the Pascal’s triangle of n
    """
    pascal = []
    for i in range(n):
        row = [1]  # start with 1 by default

        if i >= 1:
            for j in range(i):
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)
        pascal.append(row)

    return pascal
