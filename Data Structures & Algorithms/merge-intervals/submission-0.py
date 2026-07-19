class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in intervals[1:]:
            last_interval = result[-1]

            # No overlap
            if i[0] > last_interval[1]:
                result.append(i)

            # Overlap: extend the current interval if needed
            else:
                last_interval[1] = max(last_interval[1], i[1])

        return result