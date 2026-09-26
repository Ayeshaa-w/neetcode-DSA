from collections import defaultdict
def giftpacking(N,k,A):
    dp=[[float('-inf')]*(k+1) for _ in range(N+1)]
    dp[N][0]=0
    for idx in range(N-1,-1,-1):
        for k_left in range(1,k+1):
            freq=defaultdict(int)
            max_val=float('-inf')
            for j in range(idx,N-k_left+1):
                freq[A[j]]+=1
                remaining=dp[j+1][k_left-1]
                max_val=max(max_val,len(freq)+remaining)
            dp[idx][k_left]=max_val
    return dp[0][k] if dp[0][k]!=float('-inf') else 0
    def solve(idx,k_left):
        if k_left==0 and idx==N:
            return 0
        if k_left==0 or idx==N:
            return float('-inf')
        freq=defaultdict(int)
        max_val=float('-inf')
        for j in range(idx,N-k_left+1):
            freq[A[j]]+=1
            remaining=solve(j+1,k_left-1)
            max_val=max(max_val,len(freq)+remaining)
        return max_val
    return solve(0,k)
#print(giftpacking(6,3,[1,1,2,2,3,3]))
test_cases = [
    # 1. Standard Case with Repeats (Maximum distinct spread)
    {
        "name": "Standard with repeats",
        "N": 6, "k": 3, "A": [1, 1, 2, 2, 3, 3],
        "expected": 5,  # Partitions: [1], [1, 2, 2, 3], [3] -> 1 + 3 + 1 = 5
    },
    # 2. All Elements Are Unique
    {
        "name": "All unique elements",
        "N": 5, "k": 2, "A": [1, 2, 3, 4, 5],
        "expected": 5,  # Any partition sum equals N since all elements are distinct
    },
    # 3. All Elements Are Identical
    {
        "name": "All identical elements",
        "N": 5, "k": 3, "A": [7, 7, 7, 7, 7],
        "expected": 3,  # Each of the 3 partitions has exactly 1 unique element -> 1 + 1 + 1 = 3
    },
    # 4. Single Partition (k = 1)
    {
        "name": "Single partition (k=1)",
        "N": 5, "k": 1, "A": [1, 2, 1, 3, 2],
        "expected": 3,  # Total distinct elements in the entire array [1, 2, 3] = 3
    },
    # 5. k Equals N (Maximum allowed partitions)
    {
        "name": "k equals N",
        "N": 4, "k": 4, "A": [1, 2, 1, 2],
        "expected": 4,  # Each subarray is length 1 -> [1], [2], [1], [2] -> 1 + 1 + 1 + 1 = 4
    },
    # 6. Invalid Partitioning (k > N)
    {
        "name": "Impossible partition (k > N)",
        "N": 3, "k": 5, "A": [1, 2, 3],
        "expected": 0,  # Cannot form 5 non-empty partitions from 3 elements
    },
    # 7. Alternating Pattern
    {
        "name": "Alternating pattern",
        "N": 6, "k": 2, "A": [1, 2, 1, 2, 1, 2],
        "expected": 4,  # Partitions: [1, 2, 1] and [2, 1, 2] -> 2 + 2 = 4
    },
    # 8. Single Element Array (N = 1, k = 1)
    {
        "name": "Minimal input (N=1, k=1)",
        "N": 1, "k": 1, "A": [42],
        "expected": 1,  # [42] -> 1 unique element
    },
]

# Run all test cases
for idx, tc in enumerate(test_cases, 1):
    result = giftpacking(tc["N"], tc["k"], tc["A"])
    status = "PASSED" if result == tc["expected"] else f"FAILED (Got {result})"
    print(f"Test {idx} [{tc['name']}]: {status}")