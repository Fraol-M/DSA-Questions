# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
         
        """
        0 1   1 0
              
        1 0

        0 1  1 0
        1 1  1 1

        """


        row = len(mat)
        col = len(mat[0])
        
        n = len(mat)
        for _ in range(4):
            
            rotated_arr = [[0]*col for _ in range(row)]
            for r in range(row):
                for c in range(col):
                    rotated_arr[c][n-1-r]= mat[r][c] 
            
            if target == rotated_arr:
                return True
            
            mat = rotated_arr
        return False
                    
        
            
        return True


            

        