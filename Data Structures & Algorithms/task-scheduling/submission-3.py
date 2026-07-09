from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        # max heap using negative counts
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        cooldown = deque()  # (time_available, remaining_count)
        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)  # negative
                cnt += 1  # used one task

                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(heap, cnt)

        return time