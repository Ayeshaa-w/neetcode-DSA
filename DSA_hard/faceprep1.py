from collections import defaultdict
def worker(n,arr):
    end=max(arr)+1 if arr else 1
    dp=[float('-inf')]*(n+1)
    dp[n]=0
    for idx in range(n-1,-1,-1):
        hash_map=defaultdict(int)
        max_val=float('-inf')
        for j in range(idx,n):
            currsum=0
            hash_map[arr[j]]+=1
            for i in range(end+1):
                if i not in hash_map:
                    currsum=i
                    break
            score=currsum+dp[j+1]
            max_val=max(max_val,score)
        dp[idx]=max_val
    return dp[0]
    def solve(idx):
        if idx>=n:
            return 0
        if idx in memo:
            return memo[idx]
        hash_map=defaultdict(int)
        max_val=float('-inf')
        for j in range(idx,n):
            currsum=0
            hash_map[arr[j]]+=1
            for i in range(end+1):
                if i not in hash_map:
                    currsum=i
                    break
            score=currsum+solve(j+1)
            max_val=max(max_val,score)
        memo[idx]=max_val
        return max_val
    return solve(0)




if __name__ == '__main__':
    # Each tuple contains: (test_name, list_of_skills, expected_output)
    test_cases = [
        ("Example 1", [0, 2, 1, 1], 3),
        ("Example 2", [0, 1, 2, 1, 0], 5),
        ("Example 3", [0, 1, 0, 1, 1, 0, 3, 2, 1, 0], 10),
        ("Edge Case: Only Zeros", [0, 0, 0], 3),
        ("Edge Case: No Zeros", [5, 2, 9], 0)
    ]
    
    print("=== Running Custom Test Suite ===")
    for name, arr, expected in test_cases:
        n = len(arr)
        result = worker(n, arr)
        
        status = "✅" if result == expected else "❌"
        print(f"[{status}] {name}: Got {result}, Expected {expected}")