# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, emp: List['Employee'], id: int) -> int:
        

        graph = defaultdict(list)

        imp = defaultdict(int)
        for node in emp:
            val = node.id
            sub = node.subordinates
            graph[val].append(sub)
            imp[val] = node.importance

        seen = set()
        ans = 0
        def dfs(node):
            nonlocal ans
            if graph[node] == [[]]:
                return 0


            seen.add(node)
            val = graph[node][0]

    
            for ngr in val:
                dfs(ngr)
                ans+=imp[ngr]

                # print("node", ngr)
                # print("ans", ans, "imp", imp[ngr])
                # print()

                
            
            return ans

        return dfs(id) + imp[id]
     
        
            
        
            