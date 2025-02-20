# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        psum = []

        running_sum =0 

        result = float("-inf")


        for i in range(len(nums)):
            running_sum+=nums[i]

            result = max(result, running_sum)

            if running_sum < 0:
               
                running_sum = 0
        

        return result
