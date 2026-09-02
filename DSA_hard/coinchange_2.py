def change(amount, coins) -> int:
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

             
             
        def solve(idx,target):
            if target==0:
                return 1
            if idx>=len(coins) or target<0:
                return 0
            take=solve(idx,target-coins[idx])
            not_take=solve(idx+1,target)
            res=take + not_take
            return res
        return solve(0,amount)
print(change(4,[1,2,3]))