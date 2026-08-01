class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_cnt=1
        res=nums[0]
        for num in nums[1:]:
            if num!=res:
                max_cnt-=1
                if max_cnt<0:
                    res=num
            else:
                max_cnt+=1
        return res

        