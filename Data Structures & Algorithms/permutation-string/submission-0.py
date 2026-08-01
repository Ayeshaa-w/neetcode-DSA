class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr = []
        for char in s1:
            arr.append(char)
        
        n = len(arr)
        
        for i in range(len(s2)):
            temp = arr.copy()   # FIX 1: copy list
            
            j = i               # FIX 2: use separate pointer
            
            while j < len(s2) and s2[j] in temp:
                temp.remove(s2[j])
                
                if temp == []:
                    return True
                
                j += 1
        
        return False


        