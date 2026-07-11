from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        queue = deque()

        # Add border O cells
        for row in range(rows):
            if board[row][0] == "O":
                queue.append((row, 0))
            if board[row][cols - 1] == "O":
                queue.append((row, cols - 1))

        for col in range(cols):
            if board[0][col] == "O":
                queue.append((0, col))
            if board[rows - 1][col] == "O":
                queue.append((rows - 1, col))

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        # Mark all O cells connected to the border
        while queue:
            row, col = queue.popleft()

            if board[row][col] != "O":
                continue

            board[row][col] = "S"  # safe

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] == "O"
                ):
                    queue.append((new_row, new_col))

        # Capture surrounded regions and restore safe cells
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "S":
                    board[row][col] = "O"