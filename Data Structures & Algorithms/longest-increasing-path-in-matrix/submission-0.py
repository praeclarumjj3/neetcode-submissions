class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int) -> int:
            # Already calculated for this cell
            if memo[row][col] != 0:
                return memo[row][col]

            longest = 1  # path containing only this cell

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[new_row][new_col] > matrix[row][col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(new_row, new_col)
                    )

            memo[row][col] = longest
            return longest

        answer = 0

        # The longest path may start at any cell
        for row in range(rows):
            for col in range(cols):
                answer = max(answer, dfs(row, col))

        return answer