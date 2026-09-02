from collections import defaultdict
def max_gift_packing(A: list[int], N: int, K: int) -> int:
    memo={}
    def solve(idx,k_left):
        if k_left==0 and idx==N:
            return 0
        if k_left==0 or idx==N:
            return float('-inf')
        if (idx,k_left) in memo:
            return memo[(idx,k_left)]
        distinct=float('-inf')
        freq=defaultdict(int)
        for j in range(idx,N-k_left+1):
            freq[A[j]]+=1
            next_partition=solve(j+1,k_left-1)
            if next_partition!=float('-inf'):
                distinct=max(len(freq)+next_partition,distinct)
        memo[(idx,k_left)]=distinct
        return distinct
    return solve(0,K)


print(max_gift_packing([1, 1, 2, 2, 3, 3], 6, 3))

def max_gift_packing_tabulation(A: list[int], N: int, K: int) -> int:
    # dp[idx][k_left] stores maximum score from A[idx...] using k_left boxes
    dp = [[float('-inf')] * (K + 1) for _ in range(N + 1)]

    # Base Case: 0 boxes left at index N gives score 0
    dp[N][0] = 0

    # Fill table: outer loop for k_left (1 to K), inner loop for idx (N-1 down to 0)
    for k_left in range(1, K + 1):
        for idx in range(N - 1, -1, -1):
            
            distinct = float('-inf')
            freq = {}  # Tracks distinct elements in current box A[idx...j]

            # Try all valid end positions 'j' for the box starting at 'idx'
            # Loop bound (N - k_left + 1) ensures enough elements remain for remaining boxes
            for j in range(idx, N - k_left + 1):
                freq[A[j]] = freq.get(A[j], 0) + 1  # Add element A[j] to current box
                
                next_partition = dp[j + 1][k_left - 1]
                
                if next_partition != float('-inf'):
                    distinct = max(distinct, len(freq) + next_partition)

            dp[idx][k_left] = distinct

    return dp[0][K] if dp[0][K] != float('-inf') else -1


# Test call matching your example
print(max_gift_packing_tabulation([1, 1, 2, 2, 3, 3], 6, 3))  # Outputs: 5