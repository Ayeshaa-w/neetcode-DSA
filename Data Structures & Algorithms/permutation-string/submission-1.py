class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr={}
        for char in s1:
            arr[char]=arr.get(char,0)+1
        for i in range(len(s2)):
            temp=arr.copy()
            j=i
            remaining=len(s1)
            while j<len(s2) and temp.get(s2[j],0)>0:
                temp[s2[j]]-=1
                remaining-=1
                if remaining==0:
                    return True
                j+=1
        return False
        