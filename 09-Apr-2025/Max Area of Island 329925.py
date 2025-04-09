# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        dir = [(0, 1), (-1, 0), (1, 0), (0, -1)]



        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])



        def dfs(i, j):

            if not inbound(i, j) or not grid[i][j]:
                return 0

            ans = 1
            grid[i][j] = 0
            for dx, dy in dir:
                ans += dfs(i + dx, j + dy)

            return ans 


        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    max_area = max(dfs(row, col), max_area)


        return max_area

        



            
