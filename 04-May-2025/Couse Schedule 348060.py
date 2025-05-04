# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numC: int, pre: List[List[int]]) -> bool:
        

        graph = defaultdict(list)


        for u, v in pre:
            graph[v].append(u)

        node_color = [-1]*numC
        
        def dfs(node):
           
            for nei in graph[node]:

                if node_color[nei] == -1:
                    node_color[nei] = 1
                    if not dfs(nei):
                        return False

                    node_color[nei] = 2 
                elif node_color[nei] == 1:
                    return False

            return True


        for i in range(numC):
            if node_color[i] == -1:
                node_color[i] = 1
                if not dfs(i):
                    return False
                node_color[i] = 2

        return True


        


       

