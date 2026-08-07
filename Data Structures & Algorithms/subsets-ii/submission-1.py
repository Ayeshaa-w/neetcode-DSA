class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        def dfs(i,subset):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,subset)
        dfs(0,[])
        return res
