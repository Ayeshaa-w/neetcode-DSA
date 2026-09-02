
def distinctColoring (N,grid):
    dp=[[0]*4 for _ in range(N+1)]
    for r in range(N-1,-1,-1):
        for prev_col in range(4):
            min_cost=float('inf')
            for c in range(3):
                actual_prev = prev_col if prev_col < 3 else -1
                if c!=prev_col:
                    take=grid[r][c]+dp[r+1][c]
                    min_cost=min(min_cost,take)
            dp[r][prev_col]=min_cost
    return dp[0][3]
    memo={}
    def solve(r,prev_col):
        if r>=len(grid):
            return 0
        if (r,prev_col) in memo:
            return memo[r,prev_col]
        take=float('inf')
        min_cost=float('inf')
        for c in range(N):
            if c!=prev_col:
                take=grid[r][c]+solve(r+1,c)
                min_cost=min(min_cost,take)
        memo[r,prev_col]=min_cost
        return min_cost
    return dp(0,-1)

res=(distinctColoring(3,[[3,4,9],[1,7,10],[3,1,7]]))
print(res) if res<5 else print("-1")
        

                
        
        