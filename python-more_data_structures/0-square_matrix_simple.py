#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in range(len(matrix)):
        squared_matrix.append([])
        for j in range(len(matrix[i])):
           squared_matrix[i].append(matrix[i][j]**2)
    return squared_matrix
