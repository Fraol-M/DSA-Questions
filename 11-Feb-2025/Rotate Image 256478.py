# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])

        

        """

        i, j --> j, n-1-i
        0, 1 --->1, 2
        1, 2 ---> 2, 3-1-1
        1, 1 ---> 1, 4-1-1

        """

        n = len(matrix)
        for r in range(row):
            for c in range(r, n-r-1):
                og = matrix[r][c]
                x, y = r, c


                for i in range(4):
                    x, y = y, n-1-x
                    k = matrix[x][y]
                    matrix[x][y] = og
                    og = k







