from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Reverse sorting lets us efficiently pop the smallest destination.
        for source, destination in sorted(tickets, reverse=True):
            graph[source].append(destination)

        itinerary = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            # Add an airport only after all outgoing tickets are used.
            itinerary.append(airport)

        dfs("JFK")

        # Airports were added in reverse order.
        return itinerary[::-1]