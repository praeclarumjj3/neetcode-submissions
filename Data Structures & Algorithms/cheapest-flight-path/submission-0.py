import heapq
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        graph = [[] for _ in range(n)]

        for start, end, price in flights:
            graph[start].append((end, price))

        # (total_cost, current_city, flights_taken)
        heap = [(0, src, 0)]

        while heap:
            cost, city, flights_taken = heapq.heappop(heap)

            if city == dst:
                return cost

            # k stops means at most k + 1 flights
            if flights_taken == k + 1:
                continue

            for neighbor, price in graph[city]:
                heapq.heappush(
                    heap,
                    (cost + price, neighbor, flights_taken + 1)
                )

        return -1