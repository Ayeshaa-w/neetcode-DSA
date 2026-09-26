class Solution:
    def maxWeightFrequencyBalanced(self, N: int, C: int, A: list[int], W: list[int]) -> int:
        max_val=max(W)
        pre_w=[0]*(N+1)
        for i in range(N):
            pre_w[i+1]=pre_w[i]+W[i]
        category_positions={}
        for i,cat in enumerate(A):
            if cat not in category_positions:
                category_positions[cat]=[]
            category_positions[cat].append(i)
        for cat,pos in category_positions.items():
            v_score=[1 if A[i]==cat else -1 for i in range(N)]
            pre_v=[0]*(N+1)
            for j in range(N):
                pre_v[j+1]=pre_v[j]+v_score[j]
            length=len(pos)
            for l in range(length):
                for r in range(l,length):
                    left=pos[l]
                    right=pos[r]
                    if pre_v[right+1]-pre_v[left]>0:
                        weight=pre_w[right+1]-pre_w[left]
                        max_val=max(max_val,weight)
        return max_val

def main():
    sol = Solution()

    # Test Case 1: Standard majority case
    N1, C1 = 3, 3
    A1 = [1, 2, 1]
    W1 = [10, 10, 10]
    print("Test Case 1 Output:", sol.maxWeightFrequencyBalanced(N1, C1, A1, W1))
    # Expected Output: 30

    # Test Case 2: All distinct categories (no multi-element window possible)
    N2, C2 = 3, 4
    A2 = [1, 2, 3]
    W2 = [100, 100, 100]
    print("Test Case 2 Output:", sol.maxWeightFrequencyBalanced(N2, C2, A2, W2))
    # Expected Output: 100

    # Test Case 3: Complex mixed array with negative weights
    N3, C3 = 8, 3
    A3 = [1, 2, 1, 3, 1, 1, 2, 2]
    W3 = [15, -20, 10, 5, 25, -5, 30, 40]
    print("Test Case 3 Output:", sol.maxWeightFrequencyBalanced(N3, C3, A3, W3))
    # Expected Output: 70

    # Test Case 4: All negative weights
    N4, C4 = 4, 2
    A4 = [1, 1, 2, 1]
    W4 = [-10, -5, -20, -1]
    print("Test Case 4 Output:", sol.maxWeightFrequencyBalanced(N4, C4, A4, W4))
    # Expected Output: -1 (Best single element window [3, 3])

    # Test Case 5: Large positive cluster followed by large negative penalty
    N5, C5 = 5, 2
    A5 = [0, 0, 0, 1, 1]
    W5 = [5, 10, 15, -50, -50]
    print("Test Case 5 Output:", sol.maxWeightFrequencyBalanced(N5, C5, A5, W5))
    # Expected Output: 30 (Window [0, 2] with sum 5 + 10 + 15)


if __name__ == '__main__':
    main()