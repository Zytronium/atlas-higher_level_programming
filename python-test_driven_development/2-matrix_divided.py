#!/usr/bin/python3
"""
    This module, from task 1, contains a function that divides all
    elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides 2 integers and returns the result
    :param matrix: a list of lists of integers or floats
    :param div: integer or float to divide numbers in the matrix by
    :return: a new matrix of the divided numbers
    """
    new_matrix = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        matrix_width = len(matrix[0])
        for item in matrix:
            if not isinstance(item, list):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/'
                    'floats')

            if len(item) != matrix_width:
                raise TypeError(
                    'Each row of the matrix must have the same size')
            for num in item:
                if not isinstance(num, int) and not isinstance(num, float):
                    raise TypeError(
                        'matrix must be a matrix (list of lists) of integers/'
                        'floats')

    else:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)

    return new_matrix
