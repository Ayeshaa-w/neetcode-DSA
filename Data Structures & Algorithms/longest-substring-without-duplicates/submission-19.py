class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxlen=0
        seen=set()
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            maxlen=max(maxlen,r-l+1)
            seen.add(s[r])
            r+=1
        return maxlen
        