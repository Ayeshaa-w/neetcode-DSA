class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarysearch(nums,target,leftbias):
            l,r=0,len(nums)-1
            i=-1
            while l<=r:
                mid=(l+r)//2
                if target>nums[mid]:
                    l=mid+1
                elif target<nums[mid]:
                    r=mid-1
                else:
                    i=mid
                    if leftbias:
                        r=mid-1
                    else:
                        l=mid+1
            return i
        left=binarysearch(nums,target,True)
        right=binarysearch(nums,target,False)
        return [left,right]
