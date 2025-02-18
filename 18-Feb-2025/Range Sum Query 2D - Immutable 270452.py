# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.new_mat = [[0]*self.col for _ in range(self.row)]

        for r in range(self.row):
            x = 0 
            for c in range(self.col):
                prev_sum = 0
                if r > 0:
                    prev_sum = self.new_mat[r-1][c]
                x+=matrix[r][c]

                self.new_mat[r][c] = x + prev_sum



        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total_sum = self.new_mat[row2][col2]
        above_sum = 0
        if row1 -1 >= 0:
            above_sum = self.new_mat[row1-1][col2]

        left_sum = 0
        additional = 0
        if col1 -1 >= 0:
            left_sum = self.new_mat[row2][col1-1]
        
        if col1-1 >= 0 and row1-1 >= 0:
            additional = self.new_mat[row1-1][col1-1]
        return total_sum - above_sum - left_sum + additional
        
        




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)