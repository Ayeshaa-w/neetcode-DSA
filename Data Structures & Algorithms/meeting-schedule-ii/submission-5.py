"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count,res=0,0
        start_interval=sorted([i.start for i in intervals])
        end_interval=sorted([i.end for i in intervals])
        s,e=0,0
        while s<len(intervals):
            if start_interval[s]<end_interval[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            res=max(count,res)
        return res