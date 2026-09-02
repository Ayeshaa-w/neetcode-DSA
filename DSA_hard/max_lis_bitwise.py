def max_lis_bitwise(N, A, OP, target):
    dp=[1]*N
    if N==0:
        return 0
    def helper(n1,n2,op):
        if op=="AND":
            return n1 & n2
        elif op=="OR":
            return n1 | n2
        else:
            return n1 ^ n2
    for i in range(N-1,-1,-1):
        for j in range(i+1,N):
            if A[i]<A[j] and helper(A[i],A[j],OP)==target:
                dp[i]=max(dp[i],1+dp[j])
    return max(dp)

# --- Test Case from Example ---
if __name__ == "__main__":
    N = 4
    A = [1, 3, 2, 4]
    OP = "AND"
    target = 0
    
    print("Longest Subsequence Length:", max_lis_bitwise(N, A, OP, target))
    # Output: 3