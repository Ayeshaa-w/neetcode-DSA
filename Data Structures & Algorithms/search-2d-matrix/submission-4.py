class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)-1
        c=len(matrix[0])-1
        top,bottom=0,r
        while top<=bottom:
            row_mid=(top+bottom)//2
            if target>matrix[row_mid][c]:
                top=row_mid+1
            elif target<matrix[row_mid][0]:
                bottom=row_mid-1
            else:
                break
        if top>bottom:
            return False
        row_mid=(top+bottom)//2
        l,r=0,c
        while l<=r:
            mid=(l+r)//2
            if target>matrix[row_mid][mid]:
                l=mid+1
            elif target<matrix[row_mid][mid]:
                r=mid-1
            else:
                return True
        return False