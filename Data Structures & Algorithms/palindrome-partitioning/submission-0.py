class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.ispalindrome(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()#loop continues after pop adds next 2 elements then proceeds wity remaining next three not a palindrome means it skips to explore
        dfs(0)
        return res
    def ispalindrome(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True