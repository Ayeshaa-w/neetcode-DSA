class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        n=len(temperatures)
        for l in range(n):
            r=l+1
            while r<n and temperatures[l]>=temperatures[r]:
                r+=1
            if r<n:
                res.append(r-l)
            else:
                res.append(0)
        return res
