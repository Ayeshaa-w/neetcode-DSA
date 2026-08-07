class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def dfs(i,subset):
            if i>=len(s):
                res.append(subset.copy())
                return
            for j in range(i,len(s)):
                string_s=s[i:j+1]
                if string_s==string_s[::-1]:
                    subset.append(string_s)
                    dfs(j+1,subset)
                    subset.pop()
        dfs(0,[])
        return res


        