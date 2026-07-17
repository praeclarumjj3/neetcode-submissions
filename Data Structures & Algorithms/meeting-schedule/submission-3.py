"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [[i.start, i.end] for i in intervals]
        if len(intervals) <= 1:
            return True

        intervals.sort()

        meeting = intervals[0]

        for i in intervals[1:]:
            if i[0] >= meeting[1]:
                meeting = i
            else:
                return False
        
        return True

