from _heapq import heapify
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap=[]
        intervals.sort()
        res,i={},0
        for q in sorted(queries):
            while i<len(intervals) and q>=intervals[i][0]:
                l,r=intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            while minheap and q>minheap[0][1]:
                heapq.heappop(minheap)
            res[q]=minheap[0][0] if minheap else -1
        return [res[q] for q in queries]
