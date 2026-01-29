#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    Args:
        board: List of list [[r, c], [r, c]] representing placed queens.
        row: Current row.
        col: Current column.
    """
    for r, c in board:
        # Check column
        if c == col:
            return False
        # Check diagonals
        if abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(row, n, board):
    """
    Recursively solve the N queens puzzle.
    Args:
        row: Current row to place queen.
        n: The size of the board (N).
        board: List containing current solution path.
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(row + 1, n, board)
            board.pop()


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
