class Solution:
    def mySqrt(self, x: int) -> int:
        res=0
        l,r=0,x
        while l<=r:
            m=l+((r-l)//2)
            if m*m>x:
                r=m-1
            elif m*m<x:
                res=m
                l=m+1
            else:
                return m
        return res
