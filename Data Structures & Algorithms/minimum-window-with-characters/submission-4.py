class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,cnt=0,0,0
        res=-1
        count=defaultdict(int)
        for c in t:
            count[c]+=1
        min_len=float('inf')
        for r in range(len(s)):
            count[s[r]]-=1
            if count[s[r]]>=0:
                cnt+=1
            while cnt==len(t):
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    res=s[l:r+1]
                count[s[l]]+=1
                if count[s[l]]>=1:
                    cnt-=1
                l+=1
        return res if res!=-1 else ""

                

        