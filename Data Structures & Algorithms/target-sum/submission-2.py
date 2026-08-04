class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum=sum(nums)
        if totalsum-target<0 or (totalsum-target)%2!=0:
            return 0
        s2=(totalsum-target)//2 #the no.of subsets we get like this the number of ways we can attain the required combination subset so we do this
        dp=[[0]*(s2+1) for _ in range(len(nums))]
        #input cases:
        if nums[0]==0:
            #both the branches will return 1 since sum=0
            dp[0][0]=2
        else:
            dp[0][0]=1 #sum is already ssatisfied so the branch we dont pick returns 1
            #if we pick unnecassary dp[0][-9]
        #base cases:
            if nums[0]<=s2:#so that val[indx]> that taking it exceeds our target s2
                dp[0][nums[0]]=1
        for i in range(1,len(nums)):
            for s in range(s2+1):
                no_take=dp[i-1][s]
                take=0
                if nums[i]<=s:
                    take=dp[i-1][s-nums[i]]
                dp[i][s]=no_take+take
        return dp[len(nums)-1][s2]

            
        