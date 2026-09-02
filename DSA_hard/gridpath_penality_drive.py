def maxNetValue(N: int, M: int, shift_fee: int, R: int, g: list[list[int]]) -> int:
    dp=[[float('-inf')]*(M+1) for _ in range(N+1)]
    for cols in range(M+1):
        dp[N][cols]=0
    for r in range(N-1,-1,-1):
        for prev_col in range(M+1):
            max_val=float('-inf')
            for c in range(M):
                value=g[r][c]+dp[r+1][c]
                if c==prev_col:
                    total_cost=value-R
                else:
                    if prev_col!=M:
                        total_cost=value-(abs(prev_col-c)*shift_fee)
                    else:
                        total_cost=value
                max_val=max(max_val,total_cost)
            dp[r][prev_col]= max_val
    return dp[0][M]

    
    def solve(r,prev_col):
        if r>=N:
            return 0
        max_val=float('-inf')
        for c in range(M):
            value=g[r][c]+solve(r+1,c)
            if c==prev_col:
                total_cost=value-R
            else:
                if prev_col!=-1:
                    total_cost=value-(abs(prev_col-c)*shift_fee)
                else:
                    total_cost=value
            max_val=max(max_val,total_cost)
        return max_val
    return solve(0,-1)
test_cases = [
    (3, 3, 2, 5, [[10, 1, 1], [1, 20, 1], [1, 1, 30]], 56),
    (3, 3, 10, 2, [[100, 1, 1], [100, 1, 1], [100, 1, 1]], 296),
    (2, 4, 3, 10, [[50, 1, 1, 1], [1, 1, 1, 100]], 141),
    (1, 4, 5, 10, [[5, 12, 3, 8]], 12)
]

for idx, (N, M, shift_fee, R, grid, expected) in enumerate(test_cases, 1):
    result = maxNetValue(N, M, shift_fee, R, grid)
    status = "PASSED ✅" if result == expected else f"FAILED ❌ (Got {result}, Expected {expected})"
    print(f"Test Case {idx}: {status}")
