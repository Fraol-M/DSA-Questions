# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()


        result = 0
        left, right = 0, len(skill)-1
        equal = skill[left] + skill[right]
        while left < right:
            if equal == skill[left]+skill[right]:
                result+= (skill[left]*skill[right])
            else:
                return -1  

            left+=1
            right-=1
        return result