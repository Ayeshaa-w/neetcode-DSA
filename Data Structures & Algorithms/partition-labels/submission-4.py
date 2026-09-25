class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indx={}
        size,end=0,0
        res=[]
        for i,c in enumerate(s):
            last_indx[c]=i
        for i,c in enumerate(s):
            size+=1
            end=max(last_indx[c],end)
            if i==end:
                res.append(size)
                size=0
        return res
        