class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        countt={}
        have=0
        string=""
        reslen=float('inf')
        for i in t:
            countt[i]=countt.get(i,0)+1
        need=len(countt)
        l=0
        for r in range(len(s)):
            c=s[r]
            window[s[r]]=window.get(c,0)+1
            if c in countt and window[c]==countt[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    reslen=(r-l+1)
                    string=s[l:r+1]
                window[s[l]]-=1
                if s[l] in countt and window[s[l]] < countt[s[l]]:
                    have-=1
                l+=1
        return string
        