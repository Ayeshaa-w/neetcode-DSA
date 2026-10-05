class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowt=defaultdict(int)
        res,reslen=[-1,-1],float('inf')
        l,have=0,0
        countt=Counter(t)
        need=len(countt)
        for r in range(len(s)):
            windowt[s[r]]+=1
            if s[r] in countt and windowt[s[r]]==countt[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                windowt[s[l]]-=1
                if s[l] in countt and windowt[s[l]]<countt[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ""