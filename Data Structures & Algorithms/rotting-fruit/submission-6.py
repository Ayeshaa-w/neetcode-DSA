import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        # STEP 1: Gather ALL rotten oranges AND count fresh oranges
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Edge Case: If there are no fresh oranges, 0 minutes are needed
        if fresh == 0:
            return 0

        time = 0

        # STEP 2: Multi-source BFS (only run while fresh oranges remain)
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rot the fresh orange
                        fresh -= 1         # Decrement remaining fresh count
                        q.append((nr, nc))
            
            time += 1  # Increment minute after completing one full level

        # If fresh oranges remain that couldn't be reached, return -1
        return time if fresh == 0 else -1