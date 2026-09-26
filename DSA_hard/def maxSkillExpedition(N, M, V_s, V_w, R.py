def maxSkillExpedition(N, M, V_s, V_w, R_s, R_w):
    def build_2dp(n,skills,weights):
        total_weight=sum(weights)
        dp=[[float('-inf')]*(total_weight+1) for _ in range(n+1)]
        dp[0][0]=0
        for s,w in zip(skills,weights):
            for c in range(n,0,-1):
                for target in range(total_weight,w-1,-1):
                    if dp[c-1][target-w]!=float('-inf'):
                        dp[c][target]=max(dp[c][target],s+dp[c-1][target-w])
        return dp,total_weight
    dp_v,sum_v=build_2dp(N,V_s,V_w)
    dp_r,sum_r=build_2dp(M,R_s,R_w)
    max_cnt=min(N,M)
    max_w=min(sum_r,sum_v)
    max_total=0
    for i in range(max_cnt+1):
        for j in range(max_w+1):
            skills_v=dp_v[i][j]
            skills_r=dp_r[i][j]
            if skills_r!=float('-inf') and skills_v!=float('-inf'):
                max_total=max(max_total,skills_v+skills_r)
    
    return max_total
    def solve(idx,count,target,memo,skills,weights,n):
        state=(idx,count,target)
        if state in memo:
            return memo[state]
        if count==0 and target==0:
            return 0
        if count<0 or target<0 or idx>=n:
            return float('-inf')
        take=skills[idx]+solve(idx+1,count-1,target-weights[idx],memo,skills,weights,n)
        not_take=solve(idx+1,count,target,memo,skills,weights,n)
        memo[state]=max(take,not_take)
        return memo[state]
    max_cnt=min(N,M)
    max_w=min(sum(V_w),sum(R_w))
    memo_v={}
    memo_r={}
    max_total=0
    for i in range(max_cnt+1):
        for j in range(max_w+1):
            skills_v=solve(0,i,j,memo_v,V_s,V_w,N)
            skills_r=solve(0,i,j,memo_r,R_s,R_w,M)
            if skills_r!=float('-inf') and skills_v!=float('-inf'):
                max_total=max(max_total,skills_v+skills_r)

    return max_total
            



# Verified Test Suite
test_cases = [
    # Test Case 1: Standard match (K=3, Weight=10)
    # V picks all 3: Skills [10, 20, 30] -> Sum 60, Weights [2, 3, 5] -> Sum 10
    # R picks all 3: Skills [15, 25, 35] -> Sum 75, Weights [1, 4, 5] -> Sum 10
    # Expected Total Skill: 60 + 75 = 135
    {
        "name": "Standard All Candidates Match (K=3, W=10)",
        "N": 3, "M": 3,
        "V_s": [10, 20, 30], "V_w": [2, 3, 5],
        "R_s": [15, 25, 35], "R_w": [1, 4, 5],
        "expected": 135
    },

    # Test Case 2: Subset Match (K=1, Weight=3)
    # V picks index 0: Skill 10, Weight 3
    # R picks index 0: Skill 15, Weight 3
    # Expected Total Skill: 10 + 15 = 25
    {
        "name": "Subset Single Candidate Match (K=1, W=3)",
        "N": 2, "M": 2,
        "V_s": [10, 20], "V_w": [3, 7],
        "R_s": [15, 25], "R_w": [3, 4],
        "expected": 25
    },

    # Test Case 3: No Common Equal Weight Possible
    # V possible weights for K=1: [3, 7] | K=2: [10]
    # R possible weights for K=1: [2, 4] | K=2: [6]
    # No matching weights for equal K -> Expected: 0
    {
        "name": "No Matching Weights Possible",
        "N": 2, "M": 2,
        "V_s": [10, 20], "V_w": [3, 7],
        "R_s": [15, 25], "R_w": [2, 4],
        "expected": 0
    },

    # Test Case 4: Prefer Higher Skill over Max K
    # K=1, W=5 -> V[2] (Skill 50, W 5) + R[2] (Skill 60, W 5) = 110
    # K=2, W=5 -> V[0,1] (Skill 10+20=30, W 2+3=5) + R[0,1] (Skill 15+25=40, W 1+4=5) = 70
    # Expected: 110 (Chooses K=1 because skill sum is higher)
    {
        "name": "Maximize Skill (Higher Skill with lower K)",
        "N": 3, "M": 3,
        "V_s": [10, 20, 50], "V_w": [2, 3, 5],
        "R_s": [15, 25, 60], "R_w": [1, 4, 5],
        "expected": 180
    },

    # Test Case 5: Minimal Input (N=1, M=1) Match
    # Single candidate per team with equal weights
    # Expected: 10 + 20 = 30
    {
        "name": "Minimal Input N=1, M=1 Match",
        "N": 1, "M": 1,
        "V_s": [10], "V_w": [5],
        "R_s": [20], "R_w": [5],
        "expected": 30
    },

    # Test Case 6: Minimal Input (N=1, M=1) Mismatch
    # Weights don't match -> Expected: 0
    {
        "name": "Minimal Input N=1, M=1 Mismatch",
        "N": 1, "M": 1,
        "V_s": [10], "V_w": [5],
        "R_s": [20], "R_w": [4],
        "expected": 0
    }
]

# Run Script
for idx, tc in enumerate(test_cases, 1):
    res = maxSkillExpedition(tc["N"], tc["M"], tc["V_s"], tc["V_w"], tc["R_s"], tc["R_w"])
    status = "PASSED ✅" if res == tc["expected"] else f"FAILED ❌ (Got {res}, Expected {tc['expected']})"
    print(f"Test Case {idx} [{tc['name']}]: {status}")