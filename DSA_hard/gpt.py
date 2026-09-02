def maxGridPathForward(N: int, M: int, g: list[list[int]]) -> int:
    dp = [[float('-inf')] * (M + 1) for _ in range(N + 1)]
    dp[N - 1][M - 1] = g[N - 1][M - 1]

    for r in range(N - 1, -1, -1):
        for c in range(M - 1, -1, -1):
            # Preserve the destination cell value
            if r == N - 1 and c == M - 1:
                continue

            right = dp[r][c + 1]
            down = dp[r + 1][c]

            row_one = r + 1
            diagonal = float('-inf')
            if row_one % 2 == 1:
                diagonal = dp[r + 1][c + 1]
            else:
                if c - 1 >= 0:
                    diagonal = dp[r + 1][c - 1]

            res = max(right, down, diagonal)

            if res != float('-inf'):
                dp[r][c] = g[r][c] + res

    return dp[0][0] if dp[0][0] != float('-inf') else -1


test_cases = [
    (2, 2, [[1, 2], [3, 4]], 8),
    (3, 3, [[1, 10, 1], [1, 1, 100], [1, 50, 1]], 163),
    (3, 3, [[5, -2, 3], [-1, 4, 2], [1, 3, 10]], 22),
    (4, 1, [[2], [5], [-3], [10]], 14),
    (1, 4, [[3, 7, 2, 5]], 17),
    (4, 4, [[2, 3, -1, 4], [1, 8, 2, 5], [6, -4, 9, 1], [3, 2, 7, 10]], 41)
]

for idx, (N, M, grid, expected) in enumerate(test_cases, 1):
    result = maxGridPathForward(N, M, grid)
    status = "PASSED ✅" if result == expected else f"FAILED ❌ (Got {result}, Expected {expected})"
    print(f"Test Case {idx}: {status}")