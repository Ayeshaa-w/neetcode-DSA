class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output=[]
        output.append(intervals[0])
        for start,end in intervals[1:]:
            last_index=output[-1][1]
            if start<=last_index:
                output[-1][1]=max(last_index,end)
            else:
                output.append([start,end])
        return output
        