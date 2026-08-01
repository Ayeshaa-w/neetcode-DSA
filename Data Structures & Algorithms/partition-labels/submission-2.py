class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        total=0
        res=[]
        seen=set()
        q=deque()
        count=Counter(s)
        for i in s:
            total+=1
            count[i]-=1
            if i not in seen:
                seen.add(i)
                q.append(i)
            while q and count[q[0]]==0:
                q.popleft()
            if not q:
                res.append(total)
                total=0
        return res
        