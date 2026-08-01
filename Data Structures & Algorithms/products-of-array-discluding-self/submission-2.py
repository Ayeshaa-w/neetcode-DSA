class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prdct=1
        zero_cnt=0
        for num in nums:
            if num:
                prdct *= num    
            else:
                zero_cnt+=1
        
        if zero_cnt >1:
            return [0]*len(nums)
        res=[0]*len(nums)
        for i,c in enumerate(nums):
            if zero_cnt:
                res[i]=0 if c else prdct
            else:
                res[i]=prdct//c
        return res

        
        