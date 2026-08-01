class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        res=[]
        size,end=0,0
        for i,c in enumerate(s):
            lastindex[c]=i
        for i,c in enumerate(s):
            size+=1
            end=max(lastindex[c],end)
            if i==end:
                res.append(size)
                size=0
        return res
        