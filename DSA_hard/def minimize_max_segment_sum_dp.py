def minimize_max_segment_sum_dp(N, K, A):
    memo = {}

    def solve(idx, k_left):
        # Base Case 1: All segments used AND all array elements processed
        if k_left == 0 and idx == N:
            return 0
        # Base Case 2: Out of segments OR reached end without using all segments
        if k_left == 0 or idx == N:
            return float('inf')  # Use inf for invalid paths when MINIMIZING

        state = (idx, k_left)
        if state in memo:
            return memo[state]

        ans = float('inf')
        current_segment_sum = 0

        # Try ending current segment at 'j'
        for j in range(idx, N - k_left + 1):
            current_segment_sum += A[j]
            
            # Solve for remaining segments starting from j + 1
            remaining_max = solve(j + 1, k_left - 1)
            
            # We want the max sum between current segment & future segments
            possible_max = max(current_segment_sum, remaining_max)
            
            # Overall goal: Minimize this maximum sum
            ans = min(ans, possible_max)

        memo[state] = ans
        return ans

    return solve(0, K)


if __name__ == "__main__":
    # Test Case 1: Standard Example
    # Optimal splits: [7, 2, 5], [10], [8] -> Max sums: 14, 10, 8 -> Output: 14
    A1 = [7, 2, 5, 10, 8]
    N1, K1 = len(A1), 3
    print("Test Case 1 Output:", minimize_max_segment_sum_dp(N1, K1, A1))  # Expected: 14

    # Test Case 2: K = 1 (Single Segment)
    # The entire array is 1 segment -> Output: sum(A2) = 15
    A2 = [1, 2, 3, 4, 5]
    N2, K2 = len(A2), 1
    print("Test Case 2 Output:", minimize_max_segment_sum_dp(N2, K2, A2))  # Expected: 15

    # Test Case 3: K = N (Each element is its own segment)
    # Optimal splits: [1], [2], [3], [4], [5] -> Output: max(A3) = 5
    A3 = [1, 2, 3, 4, 5]
    N3, K3 = len(A3), 5
    print("Test Case 3 Output:", minimize_max_segment_sum_dp(N3, K3, A3))  # Expected: 5

    # Test Case 4: Equal Elements
    # Optimal splits: [4, 4], [4, 4], [4, 4] -> Max segment sum: 8
    A4 = [4, 4, 4, 4, 4, 4]
    N4, K4 = len(A4), 3
    print("Test Case 4 Output:", minimize_max_segment_sum_dp(N4, K4, A4))  # Expected: 8

    # Test Case 5: Large Single Bottleneck Element
    # Optimal splits: [1, 2], [100], [3, 4] -> Max segment sum: 100
    A5 = [1, 2, 100, 3, 4]
    N5, K5 = len(A5), 3
    print("Test Case 5 Output:", minimize_max_segment_sum_dp(N5, K5, A5))  # Expected: 100