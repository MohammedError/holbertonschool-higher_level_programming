#!/usr/bin/python3
import sys


def is_safe(queens, row, col):
    """
    Check if placing a queen at (row, col) is safe relative to existing queens.
    Args:
        queens: List of [r, c] pairs for placed queens.
        row: The current row.
        col: The current column.
    """
    for r, c in queens:
        if c == col:
            return False
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row, queens):
    """
    Recursive backtracking function to solve N Queens.
    Args:
        n: The size of the board.
        row: The current row being placed.
        queens: List of placed queens so far.
    """
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            # Pass a new list with the added queen to the next recursion level
            solve_nqueens(n, row + 1, queens + [[row, col]])


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

    solve_nqueens(n, 0, [])
