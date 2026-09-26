
def cutRod(price: list[int]) -> int:
    # code here
    n=len(price)
    dp=[[float('inf')]*]
    def solve(idx,target):
        if target==0:
            return 0
        if target<0 or idx>=n:
            return float('-inf')
        max_val=float('-inf')
        take=price[idx]+dp[idx][target-(idx+1)]
        if idx+1==n:
            not_take=float('-inf')
        else:
            not_take=price[idx+1]+dp[idx+1][target-(idx+2)]
        max_val=max(take,not_take)
        return max_val
    return solve(0,n)
print(cutRod([3, 5, 8, 9, 10, 17, 17, 20]))