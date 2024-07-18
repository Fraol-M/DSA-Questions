class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        status = True
        for i in range(len(matrix)-1):
            start = 0
            while start < len(matrix[i])-1:
                if matrix[i][start] != matrix[i+1][start+1]:
                    status = False
                    break
                start+=1
        return status 


        