class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=collections.deque()
        res=[]
        for r in range(len(nums)):
            while dq and nums[dq[-1]]<=nums[r]:
                dq.pop()
            dq.append(r)
            if dq[0]<r-k+1:
                dq.popleft()
            if r>=k-1:
                res.append(nums[dq[0]])
        return res
        