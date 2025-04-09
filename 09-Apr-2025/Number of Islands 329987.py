# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]



        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def dfs(i, j):
            if not inbound(i, j) or grid[i][j] != "1":
                return


            grid[i][j] = "0"

            for dx, dy in dir:
                dfs(i+dx, j+dy)

            return 

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    ans+=1 
                  

        return ans