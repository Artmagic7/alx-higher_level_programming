#!/usr/bin/python3
# task 0-square_matrix_simple.py
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for j in range(len(matrix)):
        new_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (new_matrix)
