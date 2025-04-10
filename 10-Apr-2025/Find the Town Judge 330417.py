# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        

        relation_ship = [0] * n

        for u, v in trust:
            relation_ship[u-1]-=1
            relation_ship[v-1]+=1


        print(relation_ship)
        for i in range(len(relation_ship)):
            if relation_ship[i] == n-1:
                return i+1

        return -1