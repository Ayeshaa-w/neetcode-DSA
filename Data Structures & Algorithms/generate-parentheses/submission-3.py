class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(open_,close_,subset):
            if open_==n and close_==n:
                res.append("".join(subset.copy()))
                return
            if open_ <n:
                subset.append('(')
                dfs(open_+1,close_,subset)
                subset.pop()
            if open_ and  close_<open_:
                subset.append(')')
                dfs(open_,close_+1,subset)
                subset.pop()
        dfs(0,0,[])
        return res
        