class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #got the logic confused with using two sepearte queus possible or not
        l=0
        max_len=1
        min_dq=collections.deque()
        max_dq=collections.deque()
        min_dq.append(nums[0])
        max_dq.append(nums[0])
        l=0
        for r in range(1,len(nums)):
            while min_dq and min_dq[-1]>nums[r]:
                min_dq.pop()
            while max_dq and max_dq[-1]<nums[r]:
                max_dq.pop()
            min_dq.append(nums[r])
            max_dq.append(nums[r])

            while abs(min_dq[0]-max_dq[0])>limit:
                if nums[l] ==min_dq[0]:
                    min_dq.popleft()
                elif nums[l]==max_dq[0]:
                    max_dq.popleft()
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len


