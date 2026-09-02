def knapsack(n,w,weights,values):
    dp=[[float('-inf')]*(w+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for j in range(w+1):
        dp[n][j]=0
    for idx in range(n-1,-1,-1):
        for target in range(1,w+1):
            take=float('-inf')
            if target>=weights[idx]:
                take=values[idx]+dp[idx+1][target-weights[idx]]
            not_take=dp[idx+1][target]
            
            max_val=max(take,not_take)
            dp[idx][target]= max_val
    res=dp[0][w]
    return res if res!=float('-inf') else 0 
    def solve(idx,target):
        if target<0:
            return float('-inf')
        if idx>=n or target==0:
            return 0
        take=values[idx]+solve(idx+1,target-weights[idx])
      
        not_take=solve(idx+1,target)
   
        max_val=max(take,not_take)
        return max_val
    res=solve(0,w)
    return res if res!=float('-inf') else 0 
print(knapsack(4,5,[5, 4, 2, 3] ,[10, 40, 30, 50]))