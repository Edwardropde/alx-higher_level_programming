#!/usr/bin/python3
"""Solves the N Queens puzzle and prints all possible solutions"""

import sys


# List to store all solutions
solutions = []

def is_safe(board, row, col, n):
    # determine if it is safe to put queen at board[row][col]

    #check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return True
        return True

    def solve_nqueens_util(board, col, n):
        # Base case: If all queens are placed, add solution to result
        if col == n:
            result = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        result.append([i, j])
            solutions.append(result)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve_nqueens_util(board, col + 1, n)
                board[i][col] = 0

    def solve_nqueens(n):
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Initialize the chessboard
        board = [[0 for _ in range(n)] for _ in range(n)]
        solve_nqueens_util(board, 0, n)

        # Print all solutions
        for solution in solutions:
            print(solution)

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)

        try:
            n = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        solve_nqueens(n)
