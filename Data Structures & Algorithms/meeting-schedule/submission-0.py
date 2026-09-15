"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x:x.start)
        

        prv_meet = float('-inf')

        for meet in intervals:
            if meet.start<prv_meet:
                return False
            prv_meet = meet.end
        return True
        
