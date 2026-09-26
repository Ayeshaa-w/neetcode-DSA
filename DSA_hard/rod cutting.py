def cutRod(price):
    n=len(price)
    dp=[[0]*(n+1) for _ in range(n+1)]#since the indexing starts from 0
    for idx in range(n-1,-1,-1):
        for target in range(1,n+1):
            not_take=dp[idx+1][target]
            take=float('-inf')
            if target>=idx+1:
                take=price[idx]+dp[idx][target-(idx+1)]
            dp[idx][target]=max(take,not_take)
    return dp[0][n]
print(cutRod([1, 5, 8, 9, 10, 17, 17, 20]))