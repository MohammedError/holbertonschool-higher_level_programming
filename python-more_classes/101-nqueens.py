#!/usr/bin/python3
import sys


def is_safe(solution, row, col):
    """
    Check if a queen can be placed at (row, col)
    """
    for r, c in solution:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(row, n, solution):
    """
    Backtracking function to find solutions
    """
    if row == n:
        print(solution)
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solution.append([row, col])
            solve_nqueens(row + 1, n, solution)
            solution.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(0, n, [])
