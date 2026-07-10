class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col, visited):
            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    new_row < 0
                    or new_col < 0
                    or new_row >= rows
                    or new_col >= cols
                    or (new_row, new_col) in visited
                    or heights[new_row][new_col] < heights[row][col]
                ):
                    continue

                dfs(new_row, new_col, visited)

        # Left edge touches Pacific.
        # Right edge touches Atlantic.
        for row in range(rows):
            dfs(row, 0, pacific)
            dfs(row, cols - 1, atlantic)

        # Top edge touches Pacific.
        # Bottom edge touches Atlantic.
        for col in range(cols):
            dfs(0, col, pacific)
            dfs(rows - 1, col, atlantic)

        result = []

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result