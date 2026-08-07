class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW,COL=len(board),len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=ROW or c<0 or c>=COL or board[r][c]!=word[i]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            found=( dfs(r+1,c,i+1)or
            dfs(r,c+1,i+1)or
            dfs(r-1,c,i+1)or
            dfs(r,c-1,i+1))
            board[r][c]=temp
            return found
        for row in range(ROW):
            for col in range(COL):
                if dfs(row,col,0):
                    return True
        return False
                    
        