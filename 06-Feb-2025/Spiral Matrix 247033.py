# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        top_border = 0
        left_border = 0
        right_border = len(matrix[0])-1
        bottom_border = len(matrix)-1

        result = []
        while top_border <= bottom_border and right_border >= left_border:

            for i in range(left_border, right_border+1):
                result.append(matrix[top_border][i])
            top_border+=1

            for i in range(top_border, bottom_border+1):
                result.append(matrix[i][right_border])
            right_border-=1


            if top_border <= bottom_border:
                for i in range(right_border, left_border-1, -1):
                    result.append(matrix[bottom_border][i])
                bottom_border-=1

            if left_border <= right_border:

                for i in range(bottom_border, top_border-1, -1):
                    result.append(matrix[i][left_border])
                left_border+=1
            print(result)
        return result 

                




