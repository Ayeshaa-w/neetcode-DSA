class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        l=0
        max_=0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            max_=max(max_,r-l+1)
        return max_



        
        