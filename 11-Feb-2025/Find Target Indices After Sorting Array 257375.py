# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        lit = []
        start = 0
        while start < len(nums):
            if nums[start] == target:
                lit.append(start)
            start+=1
        return lit

        