#!/usr/bin/python3
import sys


def is_safe(solution, row, col):
    """
    Check if a queen can be placed at (row, col)
    Args:
        solution: List of placed queens [[r, c], ...]
        row: Current row
        col: Current column
    """
    for r, c in solution:
        # Check column or diagonal
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(row, n, solution):
    """
    Backtracking function to find all solutions
    Args:
        row: Current row to place queen
        n: Board size
        solution: List of placed queens so far
    """
    if row == n:
        print(solution)
        return

    for col in range(n):
        if is_safe(solution, row, col):
            # Place queen
            solution.append([row, col])
            # Recurse
            solve_nqueens(row + 1, n, solution)
            # Backtrack
            solution.pop()


if __name__ == "__main__":
    # Argument validation
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

    # Start solver
    solve_nqueens(0, n, [])
