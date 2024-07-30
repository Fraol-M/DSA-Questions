class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if c * r != len(mat) * len(mat[0]):
            return mat


        arr = [[0]*c for r in range(r)]
        col = len(mat[0])
        row = len(mat)
        
        arr1 = []

        for i in range(row):
            for j in range(col):
                arr1.append(mat[i][j])
                
        k = 0
        for i in range(r):
            for j in range(c):
                arr[i][j] = arr1[k]
                k+=1
        return arr


        

        