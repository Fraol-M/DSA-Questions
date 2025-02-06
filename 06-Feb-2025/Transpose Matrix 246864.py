# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        


        res = []

        row = len(matrix)
        col = len(matrix[0])


        for c in range(col):
            temp = []
            for r in range(row):
                temp.append(matrix[r][c])
            res.append(temp)

        return res
