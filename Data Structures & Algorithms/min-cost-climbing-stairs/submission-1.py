class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        one,two=cost[n-1],0
        cost.append(0)
        for i in range(len(cost)-3,-1,-1):
            temp=one
            one=min(cost[i]+one,cost[i]+two)
            two=temp
        return min(one,two)
        