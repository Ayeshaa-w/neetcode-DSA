class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        freq={}
        for num in nums:
            freq[num]=0
        def dfs(subset,freq):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if freq[nums[i]]!=1:
                    subset.append(nums[i])
                    freq[nums[i]]=1
                    dfs(subset,freq)
                    subset.pop()
                    freq[nums[i]]=0
        dfs([],freq)
        return res

        