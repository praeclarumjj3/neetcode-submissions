from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # (minimum required time so far, row, col)
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:
            time, row, col = heapq.heappop(min_heap)

            if (row, col) in visited:
                continue

            visited.add((row, col))

            if row == n - 1 and col == n - 1:
                return time

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < n
                    and 0 <= new_col < n
                    and (new_row, new_col) not in visited
                ):
                    new_time = max(time, grid[new_row][new_col])

                    heapq.heappush(
                        min_heap,
                        (new_time, new_row, new_col)
                    )

        return -1