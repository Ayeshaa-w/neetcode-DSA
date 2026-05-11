class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        islands=0
        visit=set()
        if not grid:
            return 0
        def bfs(r,c):
            visit.add((r,c))
            q=collections.deque()
            q.append((r,c))
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                rows,cols=q.popleft()
                for dr,dc in directions:
                    r=rows+dr
                    c=cols+dc
                    if (r in range(row) and c in range(col)  and grid[r][c]=="1" and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
        


        for r in range(row):
            for c in range(col):
                if (grid[r][c]=="1") and ((r,c) not in visit):
                    bfs(r,c)
                    islands+=1
        return islands


        