class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]#global variables
        res=[]
        def backtrack(openN,closeN):
            if openN==n and closeN==n:
                res.append("".join(stack))
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closeN)#recursive upgradation of openN value instaed of variable storing
                stack.pop()
            if closeN<openN:
                stack.append(")")
                backtrack(openN,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res

        