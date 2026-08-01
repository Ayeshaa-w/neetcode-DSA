class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left,max_left=0,0
        for char in s:
            if char=='(':
                min_left,max_left=min_left+1,max_left+1
            elif char==')':
                min_left,max_left=min_left-1,max_left-1
            else:
                min_left,max_left=min_left-1,max_left+1
            if max_left<0:
                return False
            if min_left<0:
                min_left=0
        return  min_left==0 
        