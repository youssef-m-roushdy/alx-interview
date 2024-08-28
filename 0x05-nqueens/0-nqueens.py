#!/usr/bin/python3
"""
Nqueens algorithm
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)


n = int(sys.argv[1])


if n < 4:
    print("N must be at least 4")
    exit(1)


def Nqueens():
    """
    Function to solve the N-Queens problem
    """
    nqueens = []

    def is_safe(board, row, col):
        """
        Inner function to check if a queen can be placed at board[row][col]
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        """
        Backtracking function to place queens
        """
        if row == n:
            nqueens.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    board = [-1] * n
    solve(board, 0)
    return nqueens


def print_solution(nqueens):
    """
    Function to print the solutions in the required format
    """
    for solution in nqueens:
        print([[i, solution[i]] for i in range(n)])


solutions = Nqueens()

print_solution(solutions)
