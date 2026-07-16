class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        result = []

        # right, down, left, up
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        row, col = 0, 0
        direction = 0

        for _ in range(rows * cols):
            result.append(matrix[row][col])
            matrix[row][col] = "#"

            dr, dc = directions[direction]
            next_row = row + dr
            next_col = col + dc

            # Turn right if we cannot continue.
            if (
                next_row < 0
                or next_row >= rows
                or next_col < 0
                or next_col >= cols
                or matrix[next_row][next_col] == "#"
            ):
                direction = (direction + 1) % 4
                dr, dc = directions[direction]
                next_row = row + dr
                next_col = col + dc

            row, col = next_row, next_col

        return result