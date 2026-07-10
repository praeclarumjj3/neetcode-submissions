class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def navigate(row, col):
            # Outside grid or not land
            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or grid[row][col] == 0
            ):
                return 0

            # Mark this land as visited
            grid[row][col] = 0

            area = 1

            area += navigate(row - 1, col)  # up
            area += navigate(row + 1, col)  # down
            area += navigate(row, col - 1)  # left
            area += navigate(row, col + 1)  # right

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, navigate(row, col))

        return max_area