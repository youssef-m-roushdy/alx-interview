#!/usr/bin/python3
"""
Rotates a 2D matrix by 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate 2D matrix
    """
    N = len(matrix)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp
