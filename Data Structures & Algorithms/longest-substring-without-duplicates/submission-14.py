class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chk=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in chk:
                
                chk.remove(s[l])
                l+=1
            chk.add(s[r])
            res=max(res,(r-l)+1)
        return res
        