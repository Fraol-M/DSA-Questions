# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:



        node_color = [-1]*len(graph)

        def dfs(node, c):

            for neighbour in graph[node]:
                if node_color[neighbour] == -1:
                    node_color[neighbour] = 1-c
                    if not dfs(neighbour, 1-c):
                        return False

                elif node_color[neighbour] == c:
                    return False

            return True
                    


        for i in range(len(graph)):
            if node_color[i] == -1:
                if not dfs(i, 0):
                    return False


        return True
            

            
            






        