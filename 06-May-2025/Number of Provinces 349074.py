# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isCon: List[List[int]]) -> int:
        


        """
         1        1         0       0
        (1,1)   (1,2)     (1, 3)  (1, 4)
 
         1        1          0       0
         (2, 1) (2, 2)    (2, 3)  (2, 4)

         0         0          1       1
         (3, 1)  (3,2)      (3, 3)  (3, 4)


        0--1 -- 2

        1-- [2]
        2 --[1]

        3--[4]

    
        """

        graph = defaultdict(list)

        row = len(isCon)
        col = len(isCon[0])
        for r in range(row):
            for c in range(col):
                if isCon[r][c] == 1:
                    if r+1 != c+1:
                        graph[r+1].append(c+1)

        print(graph)
        seen = set()

        def dfs(node):
            
            seen.add(node)

            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
            
            return


        cnt= 0
        for node in range(1, row+1):
            if node not in seen:
                dfs(node)
                cnt+=1

        return cnt

        



















