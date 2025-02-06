# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        

        

        for i in range(1, len(nums)):
            last = nums[i-1]
            now = nums[i]
            if now == last:
                nums[i-1] *=2
                nums[i] = 0
        


        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            right+=1
            
        return nums
            

