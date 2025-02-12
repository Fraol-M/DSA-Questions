# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        

        people.sort()

        left, right = 0, len(people)-1

        boat_cnt = 0
        while left <= right:
            if people[right] + people[left] <= limit:
                left+=1
                right-=1
                boat_cnt+=1
            else:
                boat_cnt+=1
                right-=1
        return boat_cnt
