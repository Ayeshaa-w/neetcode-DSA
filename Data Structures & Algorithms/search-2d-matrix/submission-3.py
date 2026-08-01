class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)-1
        c=len(matrix[0])-1
        top,bottom=0,r
        while top<=bottom:
            row=(top+bottom)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                break
        if not (top<=bottom):
            return False
        row=(top+bottom)//2
        l,r=0,c
        while l<=r:
            m=(l+r)//2
            if target==matrix[row][m]:
                return True
            elif target>matrix[row][m]:
                l=m+1
            elif target<matrix[row][m]:
                r=m-1
        return False

        