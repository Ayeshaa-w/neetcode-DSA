class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            totalhrs=0
            for i in piles:
                totalhrs+=math.ceil(float(i)/mid)
            if totalhrs<=h:
                r=mid-1
                res=min(res,mid)
            elif totalhrs>h:
                l=mid+1
        return res


        