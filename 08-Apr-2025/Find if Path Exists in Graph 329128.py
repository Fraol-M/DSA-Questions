# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        dic = defaultdict(list)


        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)


        visited = set()
        
        def dfs(node, dic):
            
            if node == destination:
                return True

            val = dic[node]
            
            for c in val:
                if not c in visited:
                    visited.add(c)
                    if dfs(c, dic):
                        return True

            return False


        return dfs(source, dic)

