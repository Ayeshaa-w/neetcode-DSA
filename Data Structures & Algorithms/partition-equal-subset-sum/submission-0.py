class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #equally divide the sum of arr elemets
        if sum(nums)%2==1:
            return False
        target=sum(nums)//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            next_dp=set()
            for dp_val in dp:
                if dp_val+nums[i]==target:
                    return True
                next_dp.add(dp_val+nums[i])
                next_dp.add(dp_val)
            dp=next_dp
        return  False



        