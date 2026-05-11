class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for char in s:
            if char.isalnum():
                strs+=char.lower()
        n=len(strs)
        for i in range(n//2):
            if strs[i]!=strs[n-1-i]:
                return False
        return True




        