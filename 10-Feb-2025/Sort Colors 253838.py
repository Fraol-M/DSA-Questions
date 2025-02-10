# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        blue = []
        red = []
        white = []




        for i in range(len(nums)):
            if nums[i] == 0:
                red.append(0)
            elif nums[i] == 1:
                white.append(1)
            elif nums[i] == 2:
                blue.append(2)


        i = 0
        for r in red: 
            nums[i] = 0
            i+=1
        for w in white: 
            nums[i] =1
            i+=1
        for b in blue: 
            nums[i] = 2
            i+=1

       