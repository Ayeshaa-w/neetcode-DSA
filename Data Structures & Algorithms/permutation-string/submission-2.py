class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        s1_n=Counter(s1)
        for r in range(len(s2)):
            if s2[r] in s1:
                s2_n=Counter(s2[r:r+n])
                if s1_n==s2_n:
                    return True
        return False


        