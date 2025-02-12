# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        rotation = k % len(nums)

        left = len(nums) - rotation
        

        nums[:] = nums[left:] + nums[:left]

        