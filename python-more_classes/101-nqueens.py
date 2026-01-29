#!/usr/bin/python3
import sys


def is_safe(solution, row, col):
    """Check if a queen can be placed at (row, col)"""
    for r, c in solution:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens_rec(row, n, solution, solutions):
    """Backtracking function to find solutions"""
    if row == n:
        solutions.append(solution.copy())
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solution.append([row, col])
            solve_nqueens_rec(row + 1, n, solution, solutions)
            solution.pop()


def solve_nqueens(n):
    """Return all solutions for N queens"""
    solutions = []
    solve_nqueens_rec(0, n, [], solutions)
    return solutions


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

    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)
