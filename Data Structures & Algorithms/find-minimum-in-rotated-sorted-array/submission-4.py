class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=float('inf')
        l,r=0,len(nums)-1
        if nums[0]<nums[len(nums)-1]:
            return nums[0]
        while l<=r:
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
                if l<=r and nums[l]<=nums[r]:
                    res=min(res,nums[l])
                    break
            else:
                r=m-1
        return res

        