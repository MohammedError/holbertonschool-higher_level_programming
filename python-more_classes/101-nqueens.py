#!/usr/bin/python3
import sys


def is_safe(queens, row, col):
    for r, c in queens:
        if c == col:
            return False
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row, queens):
    if row == n:
        print(queens)
        return

    for col in range(n):
        if is_safe(queens, row, col):
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
