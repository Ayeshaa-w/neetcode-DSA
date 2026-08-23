class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for idx in range(n-1,-1,-1):
            for target in range(1,amount+1):
                take=0
                if target>=coins[idx]:
                    take=dp[idx][target-coins[idx]]
                not_take=dp[idx+1][target]
                res=take+not_take
                dp[idx][target]=res
        return dp[0][amount]