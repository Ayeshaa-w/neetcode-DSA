class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax,leftmin=0,0
        for char in s:
            if char=='(':
                leftmax,leftmin=leftmax+1,leftmin+1
            elif char==')':
                leftmax,leftmin=leftmax-1,leftmin-1
            else:
                leftmax,leftmin=leftmax+1,leftmin-1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin==0
        