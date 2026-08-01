class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        m=len(matrix[0])-1
        while l<=r and m>=0:
            mid=matrix[l][m]
            if mid==target:
                return True
            elif mid<target:
                l+=1
            elif mid>target:
                m-=1
        return False
            