from collections import defaultdict
from typing import List


class CountSquares:

    def __init__(self):
        # count[(x, y)] = number of times this point was added
        self.counts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        x, y = point
        self.counts[(x, y)] += 1
        self.points.append((x, y))

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        # Treat (x2, y2) as the diagonal corner.
        for x2, y2 in self.points:
            if x2 == x or abs(x2 - x) != abs(y2 - y):
                continue

            result += (
                self.counts[(x, y2)]
                * self.counts[(x2, y)]
            )

        return result