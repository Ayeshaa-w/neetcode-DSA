class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        res=0
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c]!='1' or (r,c) in visit:
                return

            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return 
        for R in range(ROW):
            for C in range(COL):
                if grid[R][C]=='1' and (R,C) not in visit:
                    dfs(R,C)
                    res+=1
        return res


            
        