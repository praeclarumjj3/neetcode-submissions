import heapq
from typing import List

class Solution:
    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:

        intervals.sort()  # Sort by interval start

        # Process queries from smallest to largest,
        # but preserve their original indices.
        sorted_queries = sorted(
            (query, index) for index, query in enumerate(queries)
        )

        answers = [-1] * len(queries)

        # Heap entries: (interval_length, interval_end)
        min_heap = []
        interval_index = 0

        for query, original_index in sorted_queries:

            # Add every interval that could contain this query
            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
            ):
                start, end = intervals[interval_index]
                length = end - start + 1

                heapq.heappush(min_heap, (length, end))
                interval_index += 1

            # Remove intervals that end before this query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            # The smallest valid interval is at the heap top
            if min_heap:
                answers[original_index] = min_heap[0][0]

        return answers