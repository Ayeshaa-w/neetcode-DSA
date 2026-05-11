class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        lastend=intervals[0][1]
        count=0
        for start,end in intervals[1:]:
            if start<lastend:
                count+=1
                lastend=min(lastend,end)
            else:
                lastend=max(lastend,end)
        return count

        