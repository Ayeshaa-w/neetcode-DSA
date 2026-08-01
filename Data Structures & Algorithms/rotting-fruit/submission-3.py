from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        def addroom(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1):
                return
            grid[r][c] = 2   # 🔥 mark as rotten immediately
            q.append((r, c))

        # Start from all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                addroom(r + 1, c)
                addroom(r - 1, c)
                addroom(r, c + 1)
                addroom(r, c - 1)

            dist += 1

        # Check any fresh orange left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return dist - 1 if dist > 0 else 0