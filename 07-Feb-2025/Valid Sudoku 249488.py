# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        row = len(board)
        col = len(board[0])

        k = set()
        cnt = 0

        for r in range(row):
            for c in range(col):
                if board[r][c].isdigit():
                    cnt+=1
                    k.add(board[r][c])
            if len(k) !=  cnt:
                print("3")
                return False
            k.clear()
            cnt = 0

        for r in range(row):
            for c in range(col):
                if board[c][r].isdigit():
                    k.add(board[c][r])
                    cnt+=1
                
            if len(k) != cnt:
                print("2")
                return False
            k.clear()
            cnt = 0

        


        for m in range(0, 9, 3):
            for l in range(0, 9, 3):
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[m+i][l+j].isdigit():
                            k.add(board[m+i][l+j])
                            cnt+=1
                if len(k) != cnt:
                    return False
                k.clear()
                cnt = 0
        return True


       

        


