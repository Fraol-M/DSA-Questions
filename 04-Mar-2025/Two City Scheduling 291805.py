# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

        costs.sort(key=lambda x: abs(x[0]-x[1]), reverse=True)

        a_count = 0
        b_count = 0
        money = 0
        mid = len(costs) // 2


        print(costs)
        for costa, costb in costs:
            if a_count < mid and b_count< mid:
                if costa < costb:
                    money+=costa
                    a_count+=1
                else:
                    money+=costb
                    b_count+=1
                print(min(costa, costb))
                
            elif b_count < mid:
                money+=costb
            else:
                money+=costa

        return money