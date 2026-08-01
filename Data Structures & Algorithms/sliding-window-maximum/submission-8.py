class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d=collections.deque()
        l,r=0,0
        output=[]
        for r in range(len(nums)):
            while d and nums[d[-1]]<nums[r]:
                d.pop()
            d.append(r)
            if l>d[0]:
                d.popleft()
            if r+1>=k:
                output.append(nums[d[0]])
                l+=1
        return output
       