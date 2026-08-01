from collections import Counter , deque
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count=Counter(s)
        q=deque()
        seen=set()
        total=0
        res=[]
        for ch in s:
            count[ch]-=1
            total+=1
            if ch not in seen:
                seen.add(ch)
                q.append(ch)
            while q and count[q[0]]==0:
                q.popleft()
            if not q:
                res.append(total)
                total=0
        return res
        