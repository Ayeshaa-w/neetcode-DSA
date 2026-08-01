class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax,curmin=1,1
        res=float('-inf')
        for n in nums:
            temp=curmax*n
            curmax=max(curmax*n,curmin*n,n)
            curmin=min(temp,curmin*n,n)
            res=max(res,curmax,curmin)
        return res
        