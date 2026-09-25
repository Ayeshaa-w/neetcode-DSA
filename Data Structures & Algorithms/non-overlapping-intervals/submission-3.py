class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        last_indx=intervals[0][1]
        res=0
        for start,end in intervals[1:]:
            if start<last_indx:
                last_indx=min(last_indx,end)
                res+=1
            else:
                last_indx=end
        return res