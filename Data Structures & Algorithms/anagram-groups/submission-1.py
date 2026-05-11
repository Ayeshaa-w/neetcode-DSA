class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        #dict values will be list sublists
        #dict used to avoid key value error
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)
            #append is used as we are directly appending in 1 cell another sublists
        return list(res.values())
                
        