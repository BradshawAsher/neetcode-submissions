"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort intervals chronologically by their start time
        intervals.sort(key=lambda i: i.start)

        #compare each meeting with the one immediately following it
        for i in range(len(intervals)-1):
            current_meeting = intervals[i]
            next_meeting = intervals[i+1]

            #if the next meeting starts before the current one ends -> conflicts
            if next_meeting.start < current_meeting.end:
                return False

        return True
