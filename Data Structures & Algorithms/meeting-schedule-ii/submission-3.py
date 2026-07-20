import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval.start)

        # End times of meetings currently occupying rooms
        min_heap = []

        for interval in intervals:
            # The earliest-ending meeting has finished,
            # so its room can be reused.
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)

        return len(min_heap)