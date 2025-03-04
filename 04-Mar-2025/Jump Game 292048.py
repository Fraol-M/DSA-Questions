# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        target_ind = float("inf")

        """

        3 2 1 0 4
        0 1 2 3 4

        """
        
        val = 0
        end = 0
        for i, j in enumerate(nums):

            if j == 0 and i== end and i+1 < len(nums):
                return False

            



            end = max(end, i+j)

            print(end, "end", i, j)

        return True

            
            



        
        


    


       
        




        return False
