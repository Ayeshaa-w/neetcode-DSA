import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            hr=0
            for i in piles:
                hr+=math.ceil(i/k)
            return hr
        l,r=1,max(piles)
        res=0
        while l<=r:
            mid=l+((r-l)//2)
            hour=hours(mid)
            if hour<h:
                res=mid
                r=mid-1
            elif hour>h:
                l=mid+1
            else:
                res=mid
                r=mid-1
        return res


