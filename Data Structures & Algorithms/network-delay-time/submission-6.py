import heapq
from typing import List


class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        graph = {node: [] for node in range(1, n + 1)}

        for source, destination, travel_time in times:
            graph[source].append((destination, travel_time))

        # (total_time_from_k, node)
        min_heap = [(0, k)]
        shortest_time = {}

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # The first time we remove a node from the min-heap,
            # we have found its shortest path.
            if node in shortest_time:
                continue

            shortest_time[node] = current_time

            for neighbor, edge_time in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(
                        min_heap,
                        (current_time + edge_time, neighbor)
                    )

        if len(shortest_time) < n:
            return -1

        return max(shortest_time.values())