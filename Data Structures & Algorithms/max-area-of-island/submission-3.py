class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        q=collections.deque()
        visit=set()
        ROW,COL=len(grid),len(grid[0])
        def bfs(row,col):
            res=1
            q.append((row,col))
            visit.add((row,col))
            while q:
                row_popped,col_popped=q.popleft()
                for rr,rc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nw_r=row_popped+rr
                    nw_c=col_popped+rc
                    if 0<=nw_r<ROW and 0<=nw_c<COL and (nw_r,nw_c) not in visit and  grid[nw_r][nw_c]==1:
                        q.append((nw_r,nw_c))
                        visit.add((nw_r,nw_c))
                        res+=1
            return res

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    found=bfs(r,c)
                    max_area=max(max_area,found)

        return max_area