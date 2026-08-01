class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxp=max(piles)
        l,r=1,maxp
        res=r
        while l<=r:
            m=(l+r)//2
            summ=0
            i=0
            while i<len(piles):
                summ+=math.ceil(float(piles[i])/m)
                i+=1
            if summ <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
            
        return res
        