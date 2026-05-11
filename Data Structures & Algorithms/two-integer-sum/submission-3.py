class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i,c in enumerate(nums):
            if (target-c) in res:
                return [res[target-c],i]
            res[c]=i
            



        