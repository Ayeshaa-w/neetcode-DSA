class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]#array that stores permutations with default empty
        for num in nums:
            new_perms=[]
            for p in perms:
            #i dont want to alter perms since other alternative positions in p i have to try
                for i in range(len(p)+1):
                    #+1 for loop boundary exclusion
                    p_copy=p.copy()
                    p_copy.insert(i,num)
                    new_perms.append(p_copy)
            perms=new_perms
        return perms


        