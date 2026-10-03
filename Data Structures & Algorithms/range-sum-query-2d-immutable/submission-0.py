class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS=len(matrix),len(matrix[0])
        self.sumatrix=[[0]*(COLS+1) for _ in range(ROWS+1)]
        for r in range(ROWS):
            prefix=0
            for c in range(COLS):
                prefix+=matrix[r][c]
                self.sumatrix[r+1][c+1]=prefix+self.sumatrix[r][c+1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,row2,col1,col2=row1+1,row2+1,col1+1,col2+1
        bottomright=self.sumatrix[row2][col2]
        above=self.sumatrix[row1-1][col2]
        left=self.sumatrix[row2][col1-1]
        common=self.sumatrix[row1-1][col1-1]
        return bottomright-above-left+common


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)