class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Minimum known cost to connect each point to the current tree
        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = set()
        total_cost = 0

        for _ in range(n):
            # Find the cheapest unvisited point
            curr = -1

            for i in range(n):
                if i not in visited:
                    if curr == -1 or min_dist[i] < min_dist[curr]:
                        curr = i

            # Add it to the minimum spanning tree
            visited.add(curr)
            total_cost += min_dist[curr]

            # Update connection costs for remaining points
            x1, y1 = points[curr]

            for nei in range(n):
                if nei not in visited:
                    x2, y2 = points[nei]
                    distance = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[nei] = min(min_dist[nei], distance)

        return total_cost