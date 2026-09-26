from collections import defaultdict
def max_dominance_score(A, K):
    memo={}
    n=len(A)
    def solve(idx,k_left):
        if k_left==0 and idx==n:
            return 0
        if k_left==0 or idx==n:
            return float('-inf')
        state=(idx,k_left)
        if state in memo:
            return memo[state]
        max_score=float('-inf')
        freq=defaultdict(int)
        max_freq=0
        for j in range(idx,n-k_left+1):#for the case of edge cases and index out of bound conditions
            freq[A[j]]+=1
            max_freq=max(max_freq,freq[A[j]])
            next_score=solve(j+1,k_left-1)
            if next_score!=float('-inf'):
                max_score=max(max_score,max_freq+next_score)
        memo[(idx,k_left)]=max_score
        return max_score
    return solve(0,K)
A = [1, 2, 1, 3, 1]
K = 2
print("Max Dominance Score:", max_dominance_score(A, K))
        
            
            